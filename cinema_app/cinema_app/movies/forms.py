from django import forms

from cinema_app.movies.models import Movie, Ticket, Comment
from cinema_app.projections.models import Projection


class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'input-field', 'placeholder': 'Title...'}
            ),
            'image': forms.FileInput(
                attrs={'class': 'input-field'}
            ),
            'trailer_video': forms.URLInput(
                attrs={'class': 'input-field', 'placeholder': 'Trailer...'}
            ),
            'genre': forms.Select(
                attrs={'class': 'input-field'}
            ),
            'year': forms.NumberInput(
                attrs={'class': 'input-field', 'placeholder': 'Year(movie created)...'}
            ),
            'description': forms.TextInput(
                attrs={'class': 'input-field', 'placeholder': 'Description...'}
            ),
            'duration': forms.NumberInput(
                attrs={'class': 'input-field', 'placeholder': 'Movie duration(mins)...'}
            ),
            'category': forms.Select(
                attrs={'class': 'input-field'}
            )

        }


class EditMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'input-field', 'placeholder': 'Title...'}
            ),
            'image': forms.FileInput(
                attrs={'class': 'input-field'}
            ),
            'trailer_video': forms.URLInput(
                attrs={'class': 'input-field', 'placeholder': 'Trailer...'}
            ),
            'genre': forms.Select(
                attrs={'class': 'input-field'}
            ),
            'year': forms.NumberInput(
                attrs={'class': 'input-field', 'placeholder': 'Year(movie created)...'}
            ),
            'description': forms.TextInput(
                attrs={'class': 'input-field', 'placeholder': 'Description...'}
            ),
            'duration': forms.NumberInput(
                attrs={'class': 'input-field', 'placeholder': 'Movie duration(mins)...'}
            ),
            'category': forms.Select(
                attrs={'class': 'input-field'}
            )

        }


class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        exclude = ['movie']
        labels = {
            'price': 'Ticket price'
        }
        widgets = {
            'price': forms.NumberInput(
                attrs={'class': 'input-field', 'placeholder': 'Ticket price...'},
            )
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('movie', 'user',)
        labels = {
            'comment': '',
        }
        widgets = {
            'comment': forms.Textarea(
                attrs={'class': 'comment-area'}
            ),
        }


class AddProjectionForm(forms.ModelForm):
    class Meta:
        model = Projection
        fields = ['movie', 'time', ]
        widgets = {
            'movie': forms.TextInput(
                attrs={
                    'class': 'input-field',
                }
            )
        }
