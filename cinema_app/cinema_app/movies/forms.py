from django import forms

from cinema_app.movies.models import Movie, Ticket


class AddMovieForm(forms.ModelForm):
    # GENRE_ACTION = 'Action'
    # GENRE_COMEDY = 'Comedy'
    # GENRE_CRIMINAL = 'Criminal'
    # GENRE_THRILLER = 'Thriller'
    # GENRE_HORROR = 'Action'
    # GENRE_FANTASY = 'Fantasy'
    # GENRE_DRAMA = 'Drama'
    # GENRE_ADVENTURE = 'Adventure'
    # GENRE_HISTORICAL = 'Historical'
    # GENRE_DOCUMENTARY = 'Documentary'
    # GENRE_CHOICES = [(x, x) for x in (
    # GENRE_ACTION, GENRE_COMEDY, GENRE_CRIMINAL, GENRE_THRILLER, GENRE_HORROR, GENRE_FANTASY, GENRE_DRAMA,
    # GENRE_ADVENTURE, GENRE_HISTORICAL, GENRE_DOCUMENTARY)]
    # CATEGORY_B = 'B'
    # CATEGORY_C = 'C'
    # CATEGORY_D = 'D'
    # CATEGORY_CHOICES = [(x, x) for x in (CATEGORY_B, CATEGORY_C, CATEGORY_D)]
    #
    # title = forms.CharField(
    #     label='Title',
    #     widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Title...'})
    # )
    #
    # image = forms.ImageField(
    #     widget=forms.FileInput(attrs={'class': 'input-field', 'placeholder': 'Add image', 'value': 'Add image'})
    # )
    #
    # genre = forms.ChoiceField(
    #     label='Genre',
    #     widget=forms.Select(attrs={'class': 'input-field'}),
    #     choices=GENRE_CHOICES,
    # )
    #
    # year = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Year(movie created)...'})
    # )
    #
    # description = forms.CharField(
    #     widget=forms.Textarea(attrs={'class': 'input-field', 'placeholder': 'Description...'})
    # )
    #
    # duration = forms.IntegerField(
    #     widget=forms.NumberInput(attrs={'class': 'input-field', 'placeholder': 'Movie duration(mins)...'})
    # )
    #
    # category = forms.ChoiceField(
    #     widget=forms.Select(attrs={'class': 'input-field'}),
    #     choices=CATEGORY_CHOICES,
    # )

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
        widgets = {
            'price': forms.NumberInput(
                attrs={'class': 'input-field'}
            )
        }
