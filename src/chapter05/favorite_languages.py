favorite_languages = {
	'jen':'python',
	'sarah':'c' ,
	'edward':'ruby',
	'phil':'python',
}

languge = favorite_languages['sarah'].title();
print(f"Sarah's favorite language is {languge}")

point_value = favorite_languages.get('aaa','No point assigned')	
print(point_value)
