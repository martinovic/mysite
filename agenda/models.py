# -*- coding: utf-8 -*-
__prj__ = '1.0.0'
__version__ = ''
__license__ = 'GNU General Public License v3'
__author__ = 'marcelo martinovic'
__email__ = 'marcelo.martinovic@gmail.com'
__url__ = ''
__date__ = "2013-10-20"
__updated__ = "2013-11-01"


from django.db import models


class Diary(models.Model):
    '''clase modelo de la agenda'''
    PROVEEDOR = 'PR'
    CLIENTE = 'CL'
    PARTICULAR = 'PA'

    TIPO = (
            (PROVEEDOR, 'Proveedor'),
            (CLIENTE, 'Cliente'),
            (PARTICULAR, 'Particular'),
    )

    RETIRA = 'RE'
    ADOMICILIO = 'DO'
    ENTREGA = (
               (RETIRA, 'Retira'),
               (ADOMICILIO, 'Domicilio'),
    )

    PAISES = (
                  ("AF", "Afganistán"),
                  ("AL", "Albania"),
                  ("DE", "Alemania"),
                  ("AD", "Andorra"),
                  ("AO", "Angola"),
                  ("AI", "Anguilla"),
                  ("AQ", "Antártida"),
                  ("AG", "Antigua y Barbuda"),
                  ("AN", "Antillas Holandesas"),
                  ("SA", "Arabia Saudí"),
                  ("DZ", "Argelia"),
                  ("AR", "Argentina"),
                  ("AM", "Armenia"),
                  ("AW", "Aruba"),
                  ("AU", "Australia"),
                  ("AT", "Austria"),
                  ("AZ", "Azerbaiyán"),
                  ("BS", "Bahamas"),
                  ("BH", "Bahrein"),
                  ("BD", "Bangladesh"),
                  ("BB", "Barbados"),
                  ("BE", "Bélgica"),
                  ("BZ", "Belice"),
                  ("BJ", "Benin"),
                  ("BM", "Bermudas"),
                  ("BY", "Bielorrusia"),
                  ("MM", "Birmania"),
                  ("BO", "Bolivia"),
                  ("BA", "Bosnia y Herzegovina"),
                  ("BW", "Botswana"),
                  ("BR", "Brasil"),
                  ("BN", "Brunei"),
                  ("BG", "Bulgaria"),
                  ("BF", "Burkina Faso"),
                  ("BI", "Burundi"),
                  ("BT", "Bután"),
                  ("CV", "Cabo Verde"),
                  ("KH", "Camboya"),
                  ("CM", "Camerún"),
                  ("CA", "Canadá"),
                  ("TD", "Chad"),
                  ("CL", "Chile"),
                  ("CN", "China"),
                  ("CY", "Chipre"),
                  ("VA", "Ciudad del Vaticano (Santa Sede)"),
                  ("CO", "Colombia"),
                  ("KM", "Comores"),
                  ("CG", "Congo"),
                  ("CD", "Congo, República Democrática del"),
                  ("KR", "Corea"),
                  ("KP", "Corea del Norte"),
                  ("CI", "Costa de Marfíl"),
                  ("CR", "Costa Rica"),
                  ("HR", "Croacia (Hrvatska)"),
                  ("CU", "Cuba"),
                  ("DK", "Dinamarca"),
                  ("DJ", "Djibouti"),
                  ("DM", "Dominica"),
                  ("EC", "Ecuador"),
                  ("EG", "Egipto"),
                  ("SV", "El Salvador"),
                  ("AE", "Emiratos Árabes Unidos"),
                  ("ER", "Eritrea"),
                  ("SI", "Eslovenia"),
                  ("ES", "España"),
                  ("US", "Estados Unidos"),
                  ("EE", "Estonia"),
                  ("ET", "Etiopía"),
                  ("FJ", "Fiji"),
                  ("PH", "Filipinas"),
                  ("FI", "Finlandia"),
                  ("FR", "Francia"),
                  ("GA", "Gabón"),
                  ("GM", "Gambia"),
                  ("GE", "Georgia"),
                  ("GH", "Ghana"),
                  ("GI", "Gibraltar"),
                  ("GD", "Granada"),
                  ("GR", "Grecia"),
                  ("GL", "Groenlandia"),
                  ("GP", "Guadalupe"),
                  ("GU", "Guam"),
                  ("GT", "Guatemala"),
                  ("GY", "Guayana"),
                  ("GF", "Guayana Francesa"),
                  ("GN", "Guinea"),
                  ("GQ", "Guinea Ecuatorial"),
                  ("GW", "Guinea-Bissau"),
                  ("HT", "Haití"),
                  ("HN", "Honduras"),
                  ("HU", "Hungría"),
                  ("IN", "India"),
                  ("ID", "Indonesia"),
                  ("IQ", "Irak"),
                  ("IR", "Irán"),
                  ("IE", "Irlanda"),
                  ("BV", "Isla Bouvet"),
                  ("CX", "Isla de Christmas"),
                  ("IS", "Islandia"),
                  ("KY", "Islas Caimán"),
                  ("CK", "Islas Cook"),
                  ("CC", "Islas de Cocos o Keeling"),
                  ("FO", "Islas Faroe"),
                  ("HM", "Islas Heard y McDonald"),
                  ("FK", "Islas Malvinas"),
                  ("MP", "Islas Marianas del Norte"),
                  ("MH", "Islas Marshall"),
                  ("UM", "Islas menores de Estados Unidos"),
                  ("PW", "Islas Palau"),
                  ("SB", "Islas Salomón"),
                  ("SJ", "Islas Svalbard y Jan Mayen"),
                  ("TK", "Islas Tokelau"),
                  ("TC", "Islas Turks y Caicos"),
                  ("VI", "Islas Vírgenes (EE.UU.)"),
                  ("VG", "Islas Vírgenes (Reino Unido)"),
                  ("WF", "Islas Wallis y Futuna"),
                  ("IL", "Israel"),
                  ("IT", "Italia"),
                  ("JM", "Jamaica"),
                  ("JP", "Japón"),
                  ("JO", "Jordania"),
                  ("KZ", "Kazajistán"),
                  ("KE", "Kenia"),
                  ("KG", "Kirguizistán"),
                  ("KI", "Kiribati"),
                  ("KW", "Kuwait"),
                  ("LA", "Laos"),
                  ("LS", "Lesotho"),
                  ("LV", "Letonia"),
                  ("LB", "Líbano"),
                  ("LR", "Liberia"),
                  ("LY", "Libia"),
                  ("LI", "Liechtenstein"),
                  ("LT", "Lituania"),
                  ("LU", "Luxemburgo"),
                  ("MK", "Macedonia, Ex-República Yugoslava de"),
                  ("MG", "Madagascar"),
                  ("MY", "Malasia"),
                  ("MW", "Malawi"),
                  ("MV", "Maldivas"),
                  ("ML", "Malí"),
                  ("MT", "Malta"),
                  ("MA", "Marruecos"),
                  ("MQ", "Martinica"),
                  ("MU", "Mauricio"),
                  ("MR", "Mauritania"),
                  ("YT", "Mayotte"),
                  ("MX", "México"),
                  ("FM", "Micronesia"),
                  ("MD", "Moldavia"),
                  ("MC", "Mónaco"),
                  ("MN", "Mongolia"),
                  ("MS", "Montserrat"),
                  ("MZ", "Mozambique"),
                  ("NA", "Namibia"),
                  ("NR", "Nauru"),
                  ("NP", "Nepal"),
                  ("NI", "Nicaragua"),
                  ("NE", "Níger"),
                  ("NG", "Nigeria"),
                  ("NU", "Niue"),
                  ("NF", "Norfolk"),
                  ("NO", "Noruega"),
                  ("NC", "Nueva Caledonia"),
                  ("NZ", "Nueva Zelanda"),
                  ("OM", "Omán"),
                  ("NL", "Países Bajos"),
                  ("PA", "Panamá"),
                  ("PG", "Papúa Nueva Guinea"),
                  ("PK", "Paquistán"),
                  ("PY", "Paraguay"),
                  ("PE", "Perú"),
                  ("PN", "Pitcairn"),
                  ("PF", "Polinesia Francesa"),
                  ("PL", "Polonia"),
                  ("PT", "Portugal"),
                  ("PR", "Puerto Rico"),
                  ("QA", "Qatar"),
                  ("UK", "Reino Unido"),
                  ("CF", "República Centroafricana"),
                  ("CZ", "República Checa"),
                  ("ZA", "República de Sudáfrica"),
                  ("DO", "República Dominicana"),
                  ("SK", "República Eslovaca"),
                  ("RE", "Reunión"),
                  ("RW", "Ruanda"),
                  ("RO", "Rumania"),
                  ("RU", "Rusia"),
                  ("EH", "Sahara Occidental"),
                  ("KN", "Saint Kitts y Nevis"),
                  ("WS", "Samoa"),
                  ("AS", "Samoa Americana"),
                  ("SM", "San Marino"),
                  ("VC", "San Vicente y Granadinas"),
                  ("SH", "Santa Helena"),
                  ("LC", "Santa Lucía"),
                  ("ST", "Santo Tomé y Príncipe"),
                  ("SN", "Senegal"),
                  ("SC", "Seychelles"),
                  ("SL", "Sierra Leona"),
                  ("SG", "Singapur"),
                  ("SY", "Siria"),
                  ("SO", "Somalia"),
                  ("LK", "Sri Lanka"),
                  ("PM", "St. Pierre y Miquelon"),
                  ("SZ", "Suazilandia"),
                  ("SD", "Sudán"),
                  ("SE", "Suecia"),
                  ("CH", "Suiza"),
                  ("SR", "Surinam"),
                  ("TH", "Tailandia"),
                  ("TW", "Taiwán"),
                  ("TZ", "Tanzania"),
                  ("TJ", "Tayikistán"),
                  ("TF", "Territorios franceses del Sur"),
                  ("TP", "Timor Oriental"),
                  ("TG", "Togo"),
                  ("TO", "Tonga"),
                  ("TT", "Trinidad y Tobago"),
                  ("TN", "Túnez"),
                  ("TM", "Turkmenistán"),
                  ("TR", "Turquía"),
                  ("TV", "Tuvalu"),
                  ("UA", "Ucrania"),
                  ("UG", "Uganda"),
                  ("UY", "Uruguay"),
                  ("UZ", "Uzbekistán"),
                  ("VU", "Vanuatu"),
                  ("VE", "Venezuela"),
                  ("VN", "Vietnam"),
                  ("YE", "Yemen"),
                  ("YU", "Yugoslavia"),
                  ("ZM", "Zambia"),
                  ("ZW", "Zimbabue"),
        )

    PROVINCIAS = (
                    ("Buenos Aires", "Buenos Aires"),
                    ("CABA", "CABA"),
                    ("Catamarca", "Catamarca"),
                    ("Chaco", "Chaco"),
                    ("Chubut", "Chubut"),
                    ("Cordoba", "Cordoba"),
                    ("Corrientes", "Corrientes"),
                    ("Entre Rios", "Entre Rios"),
                    ("Formosa", "Formosa"),
                    ("Jujuy", "Jujuy"),
                    ("La Pampa", "La Pampa"),
                    ("La Rioja", "La Rioja"),
                    ("Mendoza", "Mendoza"),
                    ("Misiones", "Misiones"),
                    ("Neuquen", "Neuquen"),
                    ("Rio Negro", "Rio Negro"),
                    ("Salta", "Salta"),
                    ("San Juan", "San Juan"),
                    ("San Luis", "San Luis"),
                    ("Santa Cruz", "Santa Cruz"),
                    ("Santa Fe", "Santa Fe"),
                    ("Santiago del Estero", "Santiago del Estero"),
                    ("Tierra del Fuego", "Tierra del Fuego"),
                    ("Tucuman", "Tucuman"),
                    ("Exterior", "Exterior"),
                  )

    razonNombreApellido = models.CharField(max_length=200, blank=False)
    calle = models.CharField(max_length=100, blank=False)
    numero = models.CharField(max_length=10, blank=False)
    piso = models.CharField(max_length=10, blank=True)
    ciudad = models.CharField(max_length=100, blank=False)
    provincia = models.CharField(max_length=40,
                                 choices=PROVINCIAS,
                                 default='CABA')
    pais = models.CharField(max_length=2,
                            choices=PAISES,
                            default="AR")
    telefono1 = models.CharField(max_length=100, blank=False)
    telefono2 = models.CharField(max_length=100, blank=True)
    telefono3 = models.CharField(max_length=100, blank=True)
    telefono4 = models.CharField(max_length=100, blank=True)
    email1 = models.CharField(max_length=200, blank=True)
    email2 = models.CharField(max_length=200, blank=True)
    email3 = models.CharField(max_length=200, blank=True)
    tipoEntrada = models.CharField(max_length=2,
                                   choices=TIPO,
                                   default=CLIENTE)
    productos = models.CharField(max_length=200, blank=True)
    entrega = models.CharField(max_length=2,
                               choices=ENTREGA,
                               default=RETIRA)
    transportes = models.CharField(max_length=200, blank=True)
    pago = models.CharField(max_length=200, blank=True)
    banco = models.CharField(max_length=200, blank=True)
    cuit = models.CharField(max_length=50, blank=True)
    cbu = models.CharField(max_length=100, blank=True)
    horario = models.CharField(max_length=20, blank=True)
    observaciones = models.CharField(max_length=1000, blank=True)

    def __unicode__(self):
        '''permite retornar el texto'''
        return self.razonNombreApellido
