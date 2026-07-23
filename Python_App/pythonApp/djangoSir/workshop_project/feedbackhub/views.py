from django.shortcuts import render
import json
import os

from django.http import HttpRequest, HttpResponse
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import FeedbackForm

def feedback_form(request: HttpRequest):
    initial_data = {}
    last_topic = request.COOKIES.get('last_workshop_topic')

    if last_topic:
        initial_data['workshop_topic'] = last_topic

    if request.method == "POST":
        form = FeedbackForm(request.POST, request.FILES)
        print("POST Data:", request.POST)           # Data given by user

        if form.is_valid():
            attachment_path = ""
            uploaded_file = form.cleaned_data.get('attachment')

            if uploaded_file:
                save_path = os.path.join(settings.MEDIA_ROOT, 'feedback_attachments', uploaded_file.name)  # settings.MEDIA_ROOT = "media" & uploaded_file.name = "resume.pdf"
                # print(f'File Path 2: {attachment_path}')        # save_path = media/feedback_attachments/resume.pdf
                # os.makedirs(os.path.dirname(save_path),exist_ok=True)

                with open(save_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)

                attachment_path = save_path
                
            feedback_data = {
                'participant_name':form.cleaned_data['participant_name'],
                'email':form.cleaned_data['email'],
                'workshop_topic':form.cleaned_data['workshop_topic'],
                'rating':form.cleaned_data['rating'],
                'comments':form.cleaned_data['comments'],
                'attachment':attachment_path
            }

            # print(f'User gave: {feedback_data}')

            with open('feedbacks.jsonl','a') as file:
                file.write( json.dumps(feedback_data)+ "\n")

            response = redirect('feedback_success')
            response.set_cookie('last_workshop_topic', form.cleaned_data['workshop_topic'])
            return response
    else:
        form = FeedbackForm(initial=initial_data)

    return render(request, 'feedbackhub/feedback_form.html', {
            'form': form,
            'request_id': request.reference_id
        }
    )

def feedback_success(request):
    return render(request, 'feedbackhub/feedback_success.html', {
            'request_id': request.reference_id
        }
    )

def analyze_feedback(request):
    if request.method == "POST":
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')

        if rating in ['Excellent','Good']:
            level = "Positive Feedback"
        elif rating == "Average":
            level = "Review Required"
        else:
            level = (
                "Needs Immediate Attention"
            )

        return JsonResponse({
            'review_level': level
        })

    return JsonResponse({
        'error': 'Invalid Request'
    })


