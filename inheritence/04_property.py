class Rectangle:
    # Constructor: runs when object is created
    # Stores width and height as internal variables
    def __init__(self, width, height):
        self._width = width      # internal variable for width
        self._height = height    # internal variable for height
        
    # Property getter for width
    # Allows you to access width like: r.width
    @property
    def width(self):
        # Formats width value to 1 decimal place and adds 'cm'
        return f"{self._width:.1f}cm"   
    
    # Property getter for height
    @property
    def height(self):
        return f"{self._height:.1f}cm" 
    
    # Setter for width
    # Allows you to set width like: r.width = value
    @width.setter
    def width(self, new_width): 
        # Validation: width must be positive
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")    
            
    # Setter for height
    @height.setter
    def height(self, new_height): 
        # Validation: height must be positive
        if new_height > 0:
            self._height = new_height
        else: 
            print("Height must be greater than zero")     
            

# Creating object of Rectangle
r = Rectangle(3, 4)

# Using setters to change values
r.width = 10
r.height = 12

# Using getters to print formatted values
print(r.width)
print(r.height)