import numpy as np
import matplotlib.pyplot as plt

csvFile = "callNrs.csv"
lastCallNr2Check = 100100 # enter a number to what CallNr. you want to compare
firstCallNr2Check = 1
bins = 100

def create_callNr_Set(csvFile):
    loadedSet = np.loadtxt(csvFile, skiprows=1, delimiter=",") # skiprows for the header

    myCallNrs = []
    for i in loadedSet:
        if i <= lastCallNr2Check and i >= firstCallNr2Check:
            myCallNrs.append(i)

    print(f"Loaded Set with {len(myCallNrs)} Call Numbers")
    print(f"Highest Call Numbers: {max(myCallNrs)}, Lowest Call Number: {min(myCallNrs)}")

    return myCallNrs

def find_missing_CallNrs(callNrSet):
    array = [*range(firstCallNr2Check, lastCallNr2Check)] # * before range = argument-unpacking operator
    
    difference = set(array).difference(set(callNrSet)) # give me the numbers, that are not in myCallNrs
    difference = sorted(difference) # transfer set to list
    np.savetxt(f"difference-Range_({firstCallNr2Check}-{lastCallNr2Check}).csv", difference, fmt="% i") # fmt = set format to integer (fmt="% s") would be string
    
    print(f"Empty CallNrs. found: {len(difference)}, Original Set length: {len(callNrSet)}, Ratio (CallNrs per empty Space):{len(callNrSet)/len(difference)}")   
    # Ratio: if < 1: There are more empty spaces than there are CallNrs

    # with open("differences.txt", "w") as f:
    #     f.write(f"Empty CallNrs. found: {len(difference)} \nOriginal Set length: {len(callNrSet)} \nRatio (CallNrs per empty Space):{len(callNrSet)/len(difference)}")

    return difference

def draw_CallNrs(callNrSet, diffSet, bins):
    """Draws a Histplot of CallNrs"""
    plt.figure(figsize=(14,7))
    plt.hist(callNrSet, bins=bins)
    plt.title("Distribution of Call Numbers")
    plt.ylabel("Count")
    plt.xlabel("CallNr")
    # format x ticks with thousands seperator
    current_values = plt.gca().get_xticks()
    plt.gca().set_xticklabels(["{:,.0f}".format(x) for x in current_values])
    # place grid
    plt.grid(True, axis=("y"), color="r", linestyle="-", linewidth=0.1)
    # Info Text
    text = f"Highest Call Number: {int(max(callNrSet)):,} -- Lowest Call Number:  {min(callNrSet):,} -- Count of Call Numbers: {len(callNrSet):,} -- CallNrs per empty Space: {round(len(callNrSet)/len(diffSet), 2)}"
    plt.text(x=0.13, y=0.85, s=text, fontsize=12, transform=plt.gcf().transFigure) # transform for relative positioning
    # plt.text(x=0.13, y=0.815, s=f"CallNrs per empty Space: {round(len(callNrSet)/len(diffSet), 2)}", fontsize=12, transform=plt.gcf().transFigure) # transform for relative positioning
    plt.savefig(f"callNr_Range_({firstCallNr2Check}-{lastCallNr2Check})")
    plt.show()

def main():
    callNrs = create_callNr_Set(csvFile)
    difference = find_missing_CallNrs(callNrs)
    draw_CallNrs(callNrs, difference, bins)

if __name__ == "__main__":
    main()