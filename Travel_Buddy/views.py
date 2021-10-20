''' /Travel_Buddy/views.py '''

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from BookTicketApp.models import PackageDetails

def country_name(key):
    a = {
    'AD': 'Andorra',
    'AE': 'United Arab Emirates',
    'AF': 'Afghanistan',
    'AG': 'Antigua & Barbuda',
    'AI': 'Anguilla',
    'AL': 'Albania',
    'AM': 'Armenia',
    'AN': 'Netherlands Antilles',
    'AO': 'Angola',
    'AQ': 'Antarctica',
    'AR': 'Argentina',
    'AS': 'American Samoa',
    'AT': 'Austria',
    'AU': 'Australia',
    'AW': 'Aruba',
    'AZ': 'Azerbaijan',
    'BA': 'Bosnia and Herzegovina',
    'BB': 'Barbados',
    'BD': 'Bangladesh',
    'BE': 'Belgium',
    'BF': 'Burkina Faso',
    'BG': 'Bulgaria',
    'BH': 'Bahrain',
    'BI': 'Burundi',
    'BJ': 'Benin',
    'BM': 'Bermuda',
    'BN': 'Brunei Darussalam',
    'BO': 'Bolivia',
    'BR': 'Brazil',
    'BS': 'Bahama',
    'BT': 'Bhutan',
    'BV': 'Bouvet Island',
    'BW': 'Botswana',
    'BY': 'Belarus',
    'BZ': 'Belize',
    'CA': 'Canada',
    'CC': 'Cocos Keeling) Islands',
    'CF': 'Central African Republic',
    'CG': 'Congo',
    'CH': 'Switzerland',
    'CI': 'Ivory Coast',
    'CK': 'Cook Iislands',
    'CL': 'Chile',
    'CM': 'Cameroon',
    'CN': 'China',
    'CO': 'Colombia',
    'CR': 'Costa Rica',
    'CU': 'Cuba',
    'CV': 'Cape Verde',
    'CX': 'Christmas Island',
    'CY': 'Cyprus',
    'CZ': 'Czech Republic',
    'DE': 'Germany',
    'DJ': 'Djibouti',
    'DK': 'Denmark',
    'DM': 'Dominica',
    'DO': 'Dominican Republic',
    'DZ': 'Algeria',
    'EC': 'Ecuador',
    'EE': 'Estonia',
    'EG': 'Egypt',
    'EH': 'Western Sahara',
    'ER': 'Eritrea',
    'ES': 'Spain',
    'ET': 'Ethiopia',
    'FI': 'Finland',
    'FJ': 'Fiji',
    'FK': 'Falkland Islands Malvinas)',
    'FM': 'Micronesia',
    'FO': 'Faroe Islands',
    'FR': 'France',
    'FX': 'France: Metropolitan',
    'GA': 'Gabon',
    'GB': 'United Kingdom Great Britain)',
    'GD': 'Grenada',
    'GE': 'Georgia',
    'GF': 'French Guiana',
    'GH': 'Ghana',
    'GI': 'Gibraltar',
    'GL': 'Greenland',
    'GM': 'Gambia',
    'GN': 'Guinea',
    'GP': 'Guadeloupe',
    'GQ': 'Equatorial Guinea',
    'GR': 'Greece',
    'GS': 'South Georgia and the South Sandwich Islands',
    'GT': 'Guatemala',
    'GU': 'Guam',
    'GW': 'Guinea-Bissau',
    'GY': 'Guyana',
    'HK': 'Hong Kong',
    'HM': 'Heard & McDonald Islands',
    'HN': 'Honduras',
    'HR': 'Croatia',
    'HT': 'Haiti',
    'HU': 'Hungary',
    'ID': 'Indonesia',
    'IE': 'Ireland',
    'IL': 'Israel',
    'IN': 'India',
    'IO': 'British Indian Ocean Territory',
    'IQ': 'Iraq',
    'IR': 'Islamic Republic of Iran',
    'IS': 'Iceland',
    'IT': 'Italy',
    'JM': 'Jamaica',
    'JO': 'Jordan',
    'JP': 'Japan',
    'KE': 'Kenya',
    'KG': 'Kyrgyzstan',
    'KH': 'Cambodia',
    'KI': 'Kiribati',
    'KM': 'Comoros',
    'KN': 'St. Kitts and Nevis',
    'KP': 'Korea: Democratic People\'s Republic of',
    'KR': 'Korea: Republic of',
    'KW': 'Kuwait',
    'KY': 'Cayman Islands',
    'KZ': 'Kazakhstan',
    'LA': 'Lao People\'s Democratic Republic',
    'LB': 'Lebanon',
    'LC': 'Saint Lucia',
    'LI': 'Liechtenstein',
    'LK': 'Sri Lanka',
    'LR': 'Liberia',
    'LS': 'Lesotho',
    'LT': 'Lithuania',
    'LU': 'Luxembourg',
    'LV': 'Latvia',
    'LY': 'Libyan Arab Jamahiriya',
    'MA': 'Morocco',
    'MC': 'Monaco',
    'MD': 'Moldova: Republic of',
    'MG': 'Madagascar',
    'MH': 'Marshall Islands',
    'ML': 'Mali',
    'MN': 'Mongolia',
    'MM': 'Myanmar',
    'MO': 'Macau',
    'MP': 'Northern Mariana Islands',
    'MQ': 'Martinique',
    'MR': 'Mauritania',
    'MS': 'Monserrat',
    'MT': 'Malta',
    'MU': 'Mauritius',
    'MV': 'Maldives',
    'MW': 'Malawi',
    'MX': 'Mexico',
    'MY': 'Malaysia',
    'MZ': 'Mozambique',
    'NA': 'Namibia',
    'NC': 'New Caledonia',
    'NE': 'Niger',
    'NF': 'Norfolk Island',
    'NG': 'Nigeria',
    'NI': 'Nicaragua',
    'NL': 'Netherlands',
    'NO': 'Norway',
    'NP': 'Nepal',
    'NR': 'Nauru',
    'NU': 'Niue',
    'NZ': 'New Zealand',
    'OM': 'Oman',
    'PA': 'Panama',
    'PE': 'Peru',
    'PF': 'French Polynesia',
    'PG': 'Papua New Guinea',
    'PH': 'Philippines',
    'PK': 'Pakistan',
    'PL': 'Poland',
    'PM': 'St. Pierre & Miquelon',
    'PN': 'Pitcairn',
    'PR': 'Puerto Rico',
    'PT': 'Portugal',
    'PW': 'Palau',
    'PY': 'Paraguay',
    'QA': 'Qatar',
    'RE': 'Reunion',
    'RO': 'Romania',
    'RU': 'Russian Federation',
    'RW': 'Rwanda',
    'SA': 'Saudi Arabia',
    'SB': 'Solomon Islands',
    'SC': 'Seychelles',
    'SD': 'Sudan',
    'SE': 'Sweden',
    'SG': 'Singapore',
    'SH': 'St. Helena',
    'SI': 'Slovenia',
    'SJ': 'Svalbard & Jan Mayen Islands',
    'SK': 'Slovakia',
    'SL': 'Sierra Leone',
    'SM': 'San Marino',
    'SN': 'Senegal',
    'SO': 'Somalia',
    'SR': 'Suriname',
    'ST': 'Sao Tome & Principe',
    'SV': 'El Salvador',
    'SY': 'Syrian Arab Republic',
    'SZ': 'Swaziland',
    'TC': 'Turks & Caicos Islands',
    'TD': 'Chad',
    'TF': 'French Southern Territories',
    'TG': 'Togo',
    'TH': 'Thailand',
    'TJ': 'Tajikistan',
    'TK': 'Tokelau',
    'TM': 'Turkmenistan',
    'TN': 'Tunisia',
    'TO': 'Tonga',
    'TP': 'East Timor',
    'TR': 'Turkey',
    'TT': 'Trinidad & Tobago',
    'TV': 'Tuvalu',
    'TW': 'Taiwan: Province of China',
    'TZ': 'Tanzania: United Republic of',
    'UA': 'Ukraine',
    'UG': 'Uganda',
    'UM': 'United States Minor Outlying Islands',
    'US': 'United States of America',
    'UY': 'Uruguay',
    'UZ': 'Uzbekistan',
    'VA': 'Vatican City State Holy See)',
    'VC': 'St. Vincent & the Grenadines',
    'VE': 'Venezuela',
    'VG': 'British Virgin Islands',
    'VI': 'United States Virgin Islands',
    'VN': 'Viet Nam',
    'VU': 'Vanuatu',
    'WF': 'Wallis & Futuna Islands',
    'WS': 'Samoa',
    'YE': 'Yemen',
    'YT': 'Mayotte',
    'YU': 'Yugoslavia',
    'ZA': 'South Africa',
    'ZM': 'Zambia',
    'ZR': 'Zaire',
    'ZW': 'Zimbabwe',
    'ZZ': 'Unknown or unspecified country',}
    return a[key]

# print(countrie_name("WF"))

def home(request):
	# print(request.user.tmsuser.pic.url)

	c={}
	c.update(csrf(request))
	request.session['temp'] = "xyz"
	c['packs'] = PackageDetails.objects.all()
	return render(request,'home.html',c)

def user_login(request):
	if request.method == 'POST':
		print("inside")
		username = request.POST['username']   ##don't use get method...
		password = request.POST['password']  ##don't use get method...
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/BookTicketApp/book_ticket/')
			else:
				return render(request,'login.html',{"error":"Account not active !"})
		else:
				print("someone tried to login but failed !")
				print("Username : {} and Password {} ".format(username, password))
				return render(request,'login.html',{"error":"Invalid Username or Password !"})
	else:
		c={}
		return render(request,'login.html',c)


def user_logout(request):
	logout(request)
	return render(request, 'logout.html')

def aboutus(request):
	request.session['temp'] = "xyz"
	return render(request,'aboutus.html')

def profile(request):
	country = country_name(f"{request.user.tmsuser.nationality}")
	context = {'country': country}
	request.session['temp'] = "xyz"
	return render(request,'profile.html',context)

def package_detail(request):
	request.session['temp'] = "xyz"
	return render(request,'package_detail.html')

def destinations(request):
	request.session['temp'] = "xyz"
	return render(request,'destinations.html')

def index(request):
	request.session['temp'] = "xyz"
	return render(request,'index.html')


