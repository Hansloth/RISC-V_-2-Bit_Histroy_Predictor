def get_status(status):
    if status == "NN":
        return 0
    if status == "NT":
        return 1
    if status == "TN":
        return 2
    if status == "TT":
        return 3

def renew_bc(BC, which_BC, predict_check):
    if predict_check == True:
        if BC[which_BC] == "st":
            BC[which_BC] = "st"
        elif BC[which_BC] == "wt":
            BC[which_BC] = "st"
        elif BC[which_BC] == "wn":
            BC[which_BC] = "sn"
        elif BC[which_BC] == "sn":
            BC[which_BC] = "sn"
    else:
        if BC[which_BC] == "st":
            BC[which_BC] = "wt"
        elif BC[which_BC] == "wt":
            BC[which_BC] = "wn"
        elif BC[which_BC] == "wn":
            BC[which_BC] = "wt"
        elif BC[which_BC] == "sn":
            BC[which_BC] = "wn"
    return BC

def BC_t_or_nt(BC):
    if BC == "sn" or BC == "wn":
        return "N"
    if BC == "st" or BC == "wt":
        return "T"

def next_status(status, input):
    first_char = list(status)[1]
    return first_char + input


input = "TTTTNNTNTNTNTNTNT"
print("\nInput: ", input)

#initial status
input = list(input)
BC=["sn", "sn", "sn", "sn"]
initial_status = "NN"
mispredict = 0

#start predict
status = initial_status

for i in range(len(input)):
    ground_truth = input[i]
    print(status, BC, "   Ground truth:", ground_truth,  end="")
    predict_check = bool

    if BC_t_or_nt(BC[get_status(status)]) == ground_truth:
        predict_check = True
        print("  Predict:", BC_t_or_nt(BC[get_status(status)]), "    predict correct", end="")
        BC = renew_bc(BC, get_status(status), predict_check)
    else:
        predict_check = False
        print("  Predict:", BC_t_or_nt(BC[get_status(status)]), "    predict wrong  ", end="")
        BC = renew_bc(BC, get_status(status), predict_check)
        mispredict += 1

    print("   Mispredict count = ", mispredict)
    status = next_status(status, input[i])

