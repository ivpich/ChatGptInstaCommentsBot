from transformers import BertForSequenceClassification, BertTokenizer
import torch
import numpy as np
import warnings

warnings.filterwarnings("ignore", message=".*UntypedStorage.*")

model = BertForSequenceClassification.from_pretrained('./to_answer_classification_model/model/pretrained_model')
tokenizer = BertTokenizer.from_pretrained('./to_answer_classification_model/model/pretrained_tokenizer')
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def decide_to_reply(comment, model, tokenizer, device):
    inputs = tokenizer.encode_plus(
        comment,
        None,
        add_special_tokens=True,
        max_length=225,
        padding='max_length',
        return_token_type_ids=True,
        truncation=True,
        return_attention_mask=True,
        return_tensors='pt',
    )

    ids = inputs['input_ids'].to(device, dtype=torch.long)
    mask = inputs['attention_mask'].to(device, dtype=torch.long)

    model.eval()
    with torch.no_grad():
        outputs = model(ids, attention_mask=mask)
        preds = torch.sigmoid(outputs.logits).cpu().detach().numpy()
        decision = np.argmax(preds, axis=1)[0]

    return decision
