from django.utils.translation import gettext_lazy as _
from django.db import models


class CountryInWorldChoices(models.TextChoices):
    IN = 'IN', _('India')
    OTH = 'OTH', _('Others')

class StateInIndiaChoices(models.TextChoices):
    AN = 'AN', _('Andaman and Nicobar Islands')
    AP = 'AP', _('Andhra Pradesh')
    AR = 'AR', _('Arunachal Pradesh')
    AS = 'AS', _('Assam')
    BR = 'BR', _('Bihar')
    CH = 'CH', _('Chandigarh')
    CT = 'CT', _('Chhattisgarh')
    DN = 'DN', _('Dadra and Nagar Haveli')
    DD = 'DD', _('Daman and Diu')
    DL = 'DL', _('Delhi')
    GA = 'GA', _('Goa')
    GJ = 'GJ', _('Gujarat')
    HR = 'HR', _('Haryana')
    HP = 'HP', _('Himachal Pradesh')
    JK = 'JK', _('Jammu and Kashmir')
    JH = 'JH', _('Jharkhand')
    KA = 'KA', _('Karnataka')
    KL = 'KL', _('Kerala')
    LD = 'LD', _('Lakshadweep')
    MP = 'MP', _('Madhya Pradesh')
    MH = 'MH', _('Maharashtra')
    MN   = 'MN', _('Manipur')
    ML = 'ML', _('Meghalaya')
    MZ = 'MZ', _('Mizoram')
    NL = 'NL', _('Nagaland')
    OR = 'OR', _('Odisha')
    PY = 'PY', _('Puducherry')
    PB = 'PB', _('Punjab')
    RJ = 'RJ', _('Rajasthan')
    SK = 'SK', _('Sikkim')
    TN = 'TN', _('Tamil Nadu')
    TG = 'TG', _('Telangana')
    TR = 'TR', _('Tripura')
    UP = 'UP', _('Uttar Pradesh')
    UT = 'UT', _('Uttarakhand')
    WB = 'WB', _('West Bengal')
    OTH = 'OTH', _('Others')


class VolunteeringForChoices(models.TextChoices):
    BLC = 'BLC', _('Blood Donation Camp')
    RHC = 'RHC', _('Rehabilation Camp')
    CRC = 'CRC', _('Child Related Camp')
    OTH = 'OTH', _('Others Activities')
    ALL = 'ALL', _('ALL')


class GetHelpForChoices(models.TextChoices):
    RHC = 'RHC', _('Rehabilitation')
    DDA = 'DDA', _('Drug De Addiction')
    SDDA = 'SDDA', _('Smoking De Addiction')
    ADA = 'ADA', _('Alcohol De-Addiction')
    MC = 'MC', _('Mental Counselling')
    OLH = 'OLH', _('Old Aged Home')
    CS = 'CS', _('Childcare Support')
    OTH = 'OTH', _('Others')