import Levenshtein

def calculate_wer(reference, hypothesis):
    reference = reference.lower().split()
    hypothesis = hypothesis.lower().split()

    # Calculate Levenshtein distance
    distance = Levenshtein.distance(" ".join(reference), " ".join(hypothesis))

    # Calculate Word Error Rate (WER)
    wer = distance / len(reference)
    return wer

# Example usage
#reference_text = "เอามาให้ตัวนี่มา เอามาให้ตัวนี้ เออ งั่ม เอาเข้าไปใกล้กว่านี้อีก เอาเข้าไปใกล้กว่านี้อีก มันงั่มไม่ได้ เออ เอาใหม่ เอาใหม่ เอาใหม่ เอาใกล้กว่านี้อีก"
#transcribed_text = "เอามาให้ตอนนี้ มามาให้ตอนนี้ มันก็ไม่ได้ เอาใหม่ เอาใหม่ เอาใหม่ เอาใกล้กว่านี้อีก"
reference_text = "But even that you see even the rock and roll dying and all that is touching someone and you know and all that was human contact if you like and now it’s not even hehehe hehe hehe"
#transcribed_text = "even roll"
transcribed_text = "Or even that you see even the rock and roll I know I hear what it was I love you"

wer = calculate_wer(reference_text, transcribed_text)
print(f"Word Error Rate (WER): {wer:.2f}%")
