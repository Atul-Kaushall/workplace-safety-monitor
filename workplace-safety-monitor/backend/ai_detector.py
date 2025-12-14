print("AI Workplace Safety Monitor Started")

def detect(image):
    if "crowd" in image:
        return "Overcrowding detected"
    if "spill" in image:
        return "Spill hazard detected"
    return "No hazard"

images = ["overcrowded.jpg", "spill.jpg"]

for img in images:
    print(img, "→", detect(img))
