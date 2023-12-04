# your_app/templatetags/rating_stars.py
from django import template

register = template.Library()

@register.filter
def rating_stars(value):
    if value is None:
        return '<i class="far fa-star"></i>' * 5  # Return 5 empty stars if value is None

    FULL_STAR = '<i class="fas fa-star"></i>'
    HALF_STAR = '<i class="fas fa-star-half-alt"></i>'
    QUARTER_STAR = '<i class="fas fa-star-quarter"></i>'
    EMPTY_STAR = '<i class="far fa-star"></i>'

    full_stars = int(value)
    remaining = value - full_stars
    half_star = 0
    quarter_star = 0

    if remaining >= 0.75:
        half_star = 1
    elif remaining >= 0.5:
        half_star = 1
    elif remaining >= 0.25:
        quarter_star = 1

    empty_stars = 5 - full_stars - half_star - quarter_star

    return FULL_STAR * full_stars + HALF_STAR * half_star + QUARTER_STAR * quarter_star + EMPTY_STAR * empty_stars
