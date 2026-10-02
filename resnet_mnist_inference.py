import torch
from datasets import load_dataset
from transformers import AutoImageProcessor, AutoModelForImageClassification

# 加载 MNIST 测试集
dataset = load_dataset("ylecun/mnist", split="test")

# 只取前 1000 个样本，加快速度
N_SAMPLES = 1000
dataset = dataset.select(range(N_SAMPLES))

# 加载预训练 ResNet-50，分类头改为 10 类（随机初始化，不微调）
model_name = "microsoft/resnet-50"
processor = AutoImageProcessor.from_pretrained(model_name)
model = AutoModelForImageClassification.from_pretrained(
    model_name,
    num_labels=10,
    ignore_mismatched_sizes=True
)
model.eval()

correct = 0
total = 0

with torch.no_grad():
    for item in dataset:
        image = item["image"]          # PIL Image, 28x28 灰度
        label = item["label"]
        image = image.convert("RGB")   # 转 3 通道
        inputs = processor(images=image, return_tensors="pt")  # resize 到 224x224
        outputs = model(**inputs)
        pred = outputs.logits.argmax(dim=-1).item()
        if pred == label:
            correct += 1
        total += 1

accuracy = correct / total
print(f"Accuracy on {total} MNIST samples: {accuracy:.4f}")
