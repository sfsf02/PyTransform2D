import numpy as np
import matplotlib.pyplot as plt

def translation_matrix( tx , ty):
    return np.array([
                    [ 1 , 0 , tx ], # for X values
                    [ 0 , 1 ,  ty ], #for Y values 
                    [ 0 , 0 ,  1 ], # for our homogenous matrix
                ])
        
def rotation_matrix( degrees ):
    theta = np.radians(degrees)
    return np.array([
        [ np.cos(theta) , -np.sin(theta) , 0 ],
        [ np.sin(theta) ,  np.cos(theta) , 0 ],
        [     0         ,     0          , 1 ]
    ])
    
def scaling_matrix( sx , sy ):
    return np.array([
                    [ sx , 0 , 0 ], # for X values
                    [ 0 , sy ,  0 ], #for Y values 
                    [ 0 , 0 ,  1 ], # for our homogenous matrix
                ])
    
def shearing_matrix( shx , shy ):
    return np.array([
                    [ 1 , shx , 0 ], # for X values
                    [ shy , 1 ,  0 ], #for Y values 
                    [ 0 , 0 ,  1 ], # for our homogenous matrix
                ])
    

if __name__ == "__main__":
    point_number=int(input("Enter the number of points : "))
    x_points = []
    y_points = []
    one_points = []
    for i in range(point_number):
        x_points.append(float(input(f"Enter the value of X{i+1}: ")))
        y_points.append(float(input(f"Enter the value of y{i+1}: ")))
        one_points.append(1)
        print("\n")
    
    if point_number >= 3:
        x_points.append(x_points[0])
        y_points.append(y_points[0])
        one_points.append(1)
       
    original_points=  np.array([ x_points , y_points , one_points ])
    master_matrix = np.eye(3) # give identity matrix  size 3x3 
    
    print("--- 2D Graphics Transformation ---")

    while True:
        print("\nOptions:")
        print("1: Add Translation")
        print("2: Add Rotation")
        print("3: Add Scaling")
        print("4: Add Shearing")
        print("5: DONE (Show Result)")
        
        choice = int(input("\nChoose an option (1-5): "))
        
        match choice:
            case 1:
                tx = float(input("Enter X translation (0 for none): "))
                ty = float(input("Enter Y translation (0 for none): "))
                T = translation_matrix(tx, ty)
                # Multiply the new matrix against the master matrix
                master_matrix = T @ master_matrix 
                print("=> Translation added!")
                
            case 2:
                angle = float(input("Enter rotation in degrees: "))
                R = rotation_matrix(angle)
                master_matrix = R @ master_matrix
                print("=> Rotation added!")
                
            case 3:
                sx = float(input("Enter X scale factor (1 for no change): "))
                sy = float(input("Enter Y scale factor (1 for no change): "))
                S = scaling_matrix(sx, sy)
                master_matrix = S @ master_matrix
                print("=> Scaling added!")
                
            case 4:
                shx = float(input("Enter X shear factor (0 for none): "))
                shy = float(input("Enter Y shear factor (0 for none): "))
                Sh = shearing_matrix(shx, shy)
                master_matrix = Sh @ master_matrix
                print("=> Shearing added!")
                
            case 5:
                print("\nApplying transformations and generating graphic...")
                break # Exit the while loop
                
            case _:
                print("Invalid option, please try again.")
                
    transformed_points = master_matrix @ original_points
    all_x = np.concatenate((original_points[0], transformed_points[0]))
    all_y = np.concatenate((original_points[1], transformed_points[1]))
                                       
    fig, axes = plt.subplots(1, 2, figsize=(8, 8))
    # --- BEFORE GRAPH ---
    axes[0].plot( original_points[0, :] , original_points[1, :] , label='Original', color='blue', linestyle='-',linewidth=2)
    axes[0].set_title('Before')
    axes[0].axhline(0, color='black', linewidth=1)
    axes[0].axvline(0, color='black', linewidth=1)
    axes[0].grid(True, linestyle=':')
    axes[0].set_xlim(min(all_x) - 2, max(all_x) + 2)
    axes[0].set_ylim(min(all_y) - 2, max(all_y) + 2)
    axes[0].set_aspect('equal', adjustable='box')
    
    # --- AFTER GRAPH ---
    axes[1].plot(transformed_points[0, :], transformed_points[1, :], label='Transformed', color='red', linestyle='-', linewidth=2)
    axes[1].set_title('After')
    axes[1].axhline(0, color='black', linewidth=1)
    axes[1].axvline(0, color='black', linewidth=1)
    axes[1].grid(True, linestyle=':')
    axes[1].set_xlim(min(all_x) - 2, max(all_x) + 2)
    axes[1].set_ylim(min(all_y) - 2, max(all_y) + 2)
    axes[1].set_aspect('equal', adjustable='box')
    
    
    plt.tight_layout() # This helps prevent the two graphs from overlapping
    plt.show()
    
    
    # (1,1),(5,1),(3,5)
    