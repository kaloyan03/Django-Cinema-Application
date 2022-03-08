from django import forms

from cinema_app.movies.models import Movie


class AddMovieForm(forms.ModelForm):
    GENRE_ACTION = 'Action'
    GENRE_COMEDY = 'Comedy'
    GENRE_CRIMINAL = 'Criminal'
    GENRE_THRILLER = 'Thriller'
    GENRE_HORROR = 'Action'
    GENRE_FANTASY = 'Fantasy'
    GENRE_DRAMA = 'Drama'
    GENRE_ADVENTURE = 'Adventure'
    GENRE_HISTORICAL = 'Historical'
    GENRE_DOCUMENTARY = 'Documentary'
    GENRE_CHOICES = [(x, x) for x in (
    GENRE_ACTION, GENRE_COMEDY, GENRE_CRIMINAL, GENRE_THRILLER, GENRE_HORROR, GENRE_FANTASY, GENRE_DRAMA,
    GENRE_ADVENTURE, GENRE_HISTORICAL, GENRE_DOCUMENTARY)]
    CATEGORY_B = 'B'
    CATEGORY_C = 'C'
    CATEGORY_D = 'D'
    CATEGORY_CHOICES = [(x, x) for x in (CATEGORY_B, CATEGORY_C, CATEGORY_D)]

    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'title-form-field input', 'placeholder': 'Title...'})
    )

    image = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'image-form-field'})
    )

    genre = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'genre-form-field input'}),
        choices=GENRE_CHOICES,
    )

    year = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Year...'})
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'input', 'placeholder': 'Description...'})
    )

    duration = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Movie duration...'})
    )

    category = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'input '}),
        choices=CATEGORY_CHOICES,
    )

    class Meta:
        model = Movie
        fields = '__all__'