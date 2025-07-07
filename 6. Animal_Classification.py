import torch
from torchvision import models, transforms
from PIL import Image

img_path = "C:/Users/ASK/Downloads/bear.jpg"
model_path = "animal_classifier.pth"
class_names = ['bear', 'elephant', 'lion', 'wolf']
img_size = 224
confidence_threshold = 0.6

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

transform = transforms.Compose([
    transforms.Resize((img_size, img_size)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

image = Image.open(img_path).convert("RGB")
image = transform(image).unsqueeze(0).to(device)

model = models.resnet18(pretrained=False)
model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))
model.load_state_dict(torch.load(model_path, map_location=device))
model = model.to(device)
model.eval()

with torch.no_grad():
    output = model(image)
    probabilities = torch.nn.functional.softmax(output, dim=1)
    confidence, predicted_idx = torch.max(probabilities, 1)
    confidence = confidence.item()
    predicted_idx = predicted_idx.item()

    if confidence >= confidence_threshold:
        predicted_class = class_names[predicted_idx]
    else:
        predicted_class = "other class"

print(f" Predicted class: {predicted_class}")
