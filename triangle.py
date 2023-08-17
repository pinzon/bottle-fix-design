import cadquery as cq

# phase 1
radius = 46.7 # mm
fin= 16.3

#box
lenght = 90
target_width =26
width=26

def weird_triangle():
    circle = cq.Workplane("XY").circle(radius).extrude(fin)
    circle=circle.translate((0,0,-fin/2))
    cube = cq.Workplane("XY").box(lenght, width, fin)

    cube2= cube.translate((0,width,0))
    cube3= cube.translate((0,width*2,0))
    cube2=cube2.union(cube3)

    circle=circle.cut(cube2)
    cube2=cube2.translate((0,-width*3,0))
    rounded_cube=circle.cut(cube2)


    # phase 2
    box = cq.Workplane("XY").box(radius, width, fin)
    box = box.translate((radius/2,0,0))

    rounded_cube=rounded_cube.cut(box)
    circle = cq.Workplane("XY").circle(18/2).extrude(fin/2, both=True)
    circle=circle.translate((-18/2,0,0))

    box = cq.Workplane("XY").box(lenght, 18, fin)
    box = box.translate((-1,17,0))
    box= box.rotate((0,0,0),(0,0,1),-6.3)

    rounded_cube=rounded_cube.cut(box)

    box = cq.Workplane("XY").box(lenght, 18, fin)
    box = box.translate((-1,-17,0))
    box= box.rotate((0,0,0),(0,0,1),6.3)
    rounded_cube=rounded_cube.cut(box)

    circle2= circle.translate((6,0,0))
    rounded_cube=rounded_cube.cut(circle2)
    circle2= circle.translate((4,0,0))
    rounded_cube=rounded_cube.cut(circle2)

    # rounded_cube=rounded_cube.add(circle)
    rounded_cube=rounded_cube.union(circle)

    # phase 3
    # rounded_cube2 = rounded_cube.translate((3,0,-3))
    # rounded_cube=rounded_cube.cut(rounded_cube2)

    return rounded_cube

show_object(weird_triangle())