import torch
from neural_network import NeuralNetwork
from text_formatter import bag_of_words, tokenizator

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


FILE = "model.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNetwork(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Наташа"
print("Привет! (Для того чтобы закончить общение введите 'выход')")
while True:
    sentence = input("ВЫ: ")
    if sentence == "выход":
        break

    sentence = tokenizator(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, prediction = torch.max(output, dim=1)

    tag = tags[prediction.item()]

    probabilities = torch.softmax(output, dim=1)
    probability = probabilities[0][prediction.item()]
    if probability.item() > 0.75:
        print(f"{bot_name}: ", tag)
    else:
        print(f"{bot_name}: Переформулируйте вопрос...")
