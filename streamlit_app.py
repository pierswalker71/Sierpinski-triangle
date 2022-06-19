
import streamlit as st

def main():
  
    import matplotlib.pyplot as plt 
    from random import choice

    # Define the three coordinate transformation methods
    def coord_change_method1(coord):
        x_new = 0.5 * coord[0]
        y_new = 0.5 * coord[1]
        return x_new, y_new

    def coord_change_method2(coord):
        x_new = 0.5 * coord[0] + 0.5
        y_new = 0.5 * coord[1] + 0.5
        return x_new, y_new

    def coord_change_method3(coord):
        x_new = 0.5 * coord[0] + 1
        y_new = 0.5 * coord[1]
        return x_new, y_new
      
    num_markers = st.number_input('number of points', min_value=100, max_value=500000, value = 100000) 

    # Generate coordinates
    x_values, y_values = [0], [0]
    x, y = 0, 0
    for i in range(num_markers):
        # Select transformation
        coord_change_method = choice([coord_change_method1,coord_change_method2,coord_change_method3])
        # Generate new coords
        x,y = coord_change_method((x, y))
        # Add new coords to list
        x_values.append(x)
        y_values.append(y)


    colours = {'red':'r','blue':'b','green':'g','yellow':'y','black':'k'}
    markers = {'point':'.', 'circle':'o', 'star':'*', 'cross':'x'}
    
    
    markersize = st.number_input('marker size', min_value=0.01, max_value=1.0, value=0.5) 
    colour = st.selectbox('colour', [x for x in colours.keys])
    marker = st.selectbox('shape', [x for x in markers.keys])'

    # Plot triangle
    fig, ax = plt.subplots(figsize=(15,15))
    marker = colours[colour] + markers[marker]

    ax.plot(x_values, y_values, marker, markersize=markersize);
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    
    
if __name__ == '__main__':
    main()