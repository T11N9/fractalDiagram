import turtle

def draw_zigzag(object1):
    for i3 in range(0, 2):       
        object1.forward(20)
        object1.right(60)
        object1.backward(20)
        object1.left(60)

def draw_fractalDiagram(object):    
    for i1 in range(0, 3):
        for i2 in range(0, 2):
            draw_zigzag(object)
            
            object.right(60)
            object.backward(20)
            object.left(60)
            object.forward(20)
            object.left(60)
            object.backward(20)
            object.right(60)    

        draw_zigzag(object)

        object.forward(20)
        object.left(120)

    object.right(60)
    object.forward(20)
    object.right(60)
    object.backward(20 * 8)
    object.right(60)
    object.forward(20 * 8)
    object.right(60)
    object.backward(20 * 7)

def draw():
    window = turtle.Screen()
    window.bgcolor("blue")
    #Create a turtle Felix
    felix = turtle.Turtle()
    felix.shape("turtle")
    felix.color("red")
    felix.speed(1)
    felix.right(180)
    draw_fractalDiagram(felix)

    window.exitonclick()

draw()    
