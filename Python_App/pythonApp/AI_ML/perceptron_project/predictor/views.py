from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .forms import PlacementPredictionForm
from .perceptron import predict_placement


def placement_prediction(request):
    prediction = None
    prediction_code = None

    if request.method == "POST":
        form = PlacementPredictionForm(request.POST)

        if form.is_valid():
            cgpa = form.cleaned_data["cgpa"]
            aptitude = form.cleaned_data["aptitude"]

            prediction_code = predict_placement(
                cgpa=cgpa,
                aptitude=aptitude,
            )

            if prediction_code == 1:
                prediction = "Student is likely to be placed."
            else:
                prediction = "Student is unlikely to be placed."

    else:
        form = PlacementPredictionForm()

    context = {
        "form": form,
        "prediction": prediction,
        "prediction_code": prediction_code,
    }

    return render(
        request,
        "predictor/predict.html",
        context,
    )