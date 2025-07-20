from fpdf import FPDF

# Create a PDF instance
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Add a Unicode font (replace with your preferred font path)
pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
pdf.set_font('DejaVu', '', 12)

# Title
pdf.set_font('DejaVu', style='B', size=16)
pdf.cell(0, 10, "Computer Graphics Notes", ln=True, align="C")
pdf.ln(10)

# Answers content
content = [ ("CIE Chromaticity", """ The CIE Chromaticity Diagram is a 2D graph that shows all the colors visible to the human eye. It is used to understand and manage color in technologies like displays and lighting. Key Points: - Represents colors as points on the diagram. - Edges show pure colors (rainbow), and inside shows mixed colors. - The center represents white light. - Useful for making displays, lighting systems, and graphics applications. """), ("RGB Color Model", """ The RGB Color Model uses Red (R), Green (G), and Blue (B) to represent colors. It is an additive model where different intensities of R, G, and B combine to create all colors. Key Points: - Each color is represented as (R, G, B), values normalized between 0 and 1. - Useful for displays, image processing, and graphics. - Example: Bright red is (1, 0, 0), and white is (1, 1, 1). """), ("HSV Color Model", """ The HSV Color Model represents colors using three components: Hue (type of color), Saturation (vividness of the color), and Value (brightness). It is more intuitive than RGB. Key Points: - Hue: Measured in degrees, represents the type of color (e.g., red = 0°, green = 120°). - Saturation: Percentage of how vivid the color is (0% = gray). - Value: Percentage of brightness (0% = black). """), ("Light Source - Ambient Light", """ Ambient Light is a uniform light source that illuminates all objects equally, without a specific direction or shadows. Key Points: - Ensures visibility for objects not directly lit by other light sources. - Provides a base brightness level for the scene. - Example: Low ambient light in a room makes everything dimly visible. """), ("Diffuse Reflection", """ Diffuse Reflection occurs when light hits a rough surface and scatters in many directions. It gives objects a uniformly lit appearance. Key Points: - Brightness depends on the angle between the light source and the surface normal. - Formula: I = k_d * I_l * cos(θ), where θ is the angle between the light and the surface. - Example: A wall lit by a bulb shows even lighting. """), ("Specular Reflection", """ Specular Reflection is the mirror-like reflection of light from a smooth surface, creating highlights. Key Points: - Brightness depends on the viewer's angle relative to the reflection direction. - Formula: I_s = k_s * I_l * (cos(α))^n, where α is the angle between viewer and reflection, and n controls highlight sharpness. """), ("Phong Specular Reflection Model", """ Phong's model calculates realistic highlights by considering the angle between the viewer, the light, and the surface normal. Formula: I = k_d * I_l * cos(θ) + k_s * I_l * (cos(α))^n - Adds diffuse and specular reflection for accurate results. - Widely used in computer graphics for shiny surfaces. """), ("Shading Algorithms", """ Shading algorithms determine how light interacts with surfaces. Types: - Flat Shading: Fast, each polygon has a single color. - Gouraud Shading: Smooth but misses small highlights, computes lighting at vertices. - Phong Shading: Most realistic, calculates lighting per pixel. """), ("Flat Shading", """ Flat Shading calculates lighting for the entire polygon and applies the same color to all its pixels. Key Points: - Fast and simple to implement. - Produces a faceted appearance. - Example: Useful in retro-style games. """), ("Gouraud Shading", """ Gouraud Shading computes lighting at each vertex and interpolates the values across the surface. Key Points: - Smooth appearance. - Might miss specular highlights. - Used in older games and real-time rendering. """), ("Phong Shading", """ Phong Shading calculates lighting per pixel, resulting in highly realistic images with smooth highlights. Key Points: - Accurate highlights and shading transitions. - Computationally expensive but ideal for high-quality rendering. """), ("Halftone Shading", """ Halftone Shading uses patterns of dots to simulate shading, often used in printing and artistic effects. Key Points: - Dots vary in size/density to represent brightness. - Artistic effect but less realistic for 3D rendering. """), ("Backface Detection and Removal", """ Backface detection identifies polygons facing away from the viewer and removes them to save computation. Key Points: - Uses the surface normal and the viewer's direction. - Reduces rendering time and eliminates unseen polygons. """), ("Depth Buffer Algorithm (Z-Buffer)", """ Z-Buffer Algorithm determines visibility by comparing pixel depths. The closest pixel is rendered. Steps: - Create a depth buffer initialized with maximum depth values. - Compare each pixel’s depth with the buffer value and update it if closer. - Outputs the visible parts of objects. """), ("Depth Sort Algorithm (Painter’s Algorithm)", """ The Painter’s Algorithm draws polygons from back to front, ensuring closer objects overwrite farther ones. Steps: - Sort polygons by depth. - Draw them in order from farthest to nearest. - Handles simple visibility but struggles with intersecting polygons. """), ("Warnock Algorithm", """ Warnock’s Algorithm is a divide-and-conquer method for hidden surface removal. Steps: - Divide the screen into smaller regions. - Resolve visibility for simple regions. - Recursively subdivide complex regions until they are simple enough to resolve. """), ]

# Adding content to the PDF
for title, text in content:
    pdf.set_font('DejaVu', style='B', size=14)
    pdf.cell(0, 10, title, ln=True)
    pdf.ln(5)
    pdf.set_font('DejaVu', '', 12)
    pdf.multi_cell(0, 10, text)
    pdf.ln(5)

# Save the PDF file
file_path = "Computer_Graphics_Notes.pdf"
pdf.output(file_path)
