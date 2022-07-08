from django.test import TestCase

# Create your tests here.
const listuser=['andai1910','andai1911','andai1912','andai1913','andai1914',
'andai1915',
'andai1916','andai1917','andai1918',
'andai1919','andai1920','andai1921','andai1922','andai1923','andai1924',
'andai1925',
'andai1926','andai1927','andai1928',
'andai1929','andai1930','andai1931','andai1932','andai1933','andai1934',
'andai1935',
'andai1936','andai1937','andai1938',
'andai1939','andai1940','andai1941','andai1942','andai1943','andai1944',
'andai1945',
'andai1946','andai1947','andai1948',
'andai1949','andai1950','andai1951','andai1952','andai1953','andai1954',
'andai1955',
'andai1956','andai1957','andai1958',
'andai1959','andai1960','andai1961','andai1962','andai1963','andai1964',
'andai1965',
'andai1966','andai1967','andai1968',
'andai1969','andai1970','andai1971','andai1972','andai1973','andai1974',
'andai1975',
'andai1976','andai1977','andai1978',
'andai1979','andai1980','andai1981','andai1982','andai1983','andai1984','andai1985',
'andai1986',
'andai1987','andai1988','andai1989','andai1990',
'andai1991','andai1992','andai1993','andai1994','andai1999']


 User.objects.bulk_create([User(username=listuser[i],password='anhdai123') for i in range(len(listuser))])