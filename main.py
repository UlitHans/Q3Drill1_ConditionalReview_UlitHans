from pyscript import document

def compute_average(event):
    # Read inputs and validate
    try:
        raw1 = document.getElementById("score1").value
        raw2 = document.getElementById("score2").value
        score1 = float(raw1) if raw1 != '' else None
        score2 = float(raw2) if raw2 != '' else None
    except Exception:
        document.getElementById("average").innerText = "N/A"
        document.getElementById("result").innerText = "Invalid input"
        return

    if score1 is None or score2 is None:
        document.getElementById("average").innerText = "N/A"
        document.getElementById("result").innerText = "Enter both scores"
        return

    average = (score1 + score2) / 2

    result = "✅ Pass" if average >= 75 else "❌ Fail"

    document.getElementById("average").innerText = f"{average:.2f}"
    document.getElementById("result").innerText = result