import cadquery as cq

result = cq.Workplane("XY").box(3, 3, 0.5).edges("|Z").fillet(0.125)


# Dimensions
outer_diameter = 52  # Outer diameter of the cap
inner_diameter = 1  # Inner diameter of the cap
height = 50  # Height of the cap

# Create a cylinder for the main body
body = cq.Workplane("XY").circle(outer_diameter / 2).extrude(height)

# Create a smaller cylinder for the inner part
inner_cylinder = cq.Workplane("XY").circle(inner_diameter / 2).extrude(height)

# Subtract the inner cylinder from the main body to create the cavity
body = body.cut(inner_cylinder)

# Create the top surface of the cap
top_surface = cq.Workplane("XY").circle(outer_diameter / 2).extrude(2)

# Translate the top surface to the correct height
top_surface = top_surface.translate((0, 0, height))

# Join the top surface with the main body
body = body.union(top_surface)

# Render the bottle cap
piece = body
