#CODED BY 0XBIT
#License: MIT

from pystyle import *
import random, os, sys
import warnings
warnings.filterwarnings('ignore')
import requests
import datetime
import threading
import string

os.system('clear')

banner = '''

                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣭⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⢰⣮⣵⣾⡥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⣀⣀⣀⣴⡿⠁⠀⠈⣿⣿⣿⢁⣴⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠾⣷⣶⣿⣿⣿⣯⣶⣶⣿⣷⠀⢹⣿⣿⢸⣯⣿⣿⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⣾⣷⣜⡿⣿⠟⠋⢸⣿⣿⡟⣱⡆⢸⣿⣿⠘⣧⠹⣿⣿⠋⣴⢶⣦⠀⠀⠀⠀⠀
                                    ⢹⣿⣿⣿⠆⠀⠀⢸⣿⣿⠃⢿⡇⢸⣿⣿⠀⣫⡀⢿⣿⡆⣱⣿⣿⡇⠀⠀⠀⠀
                                    ⠀⢻⣿⠁⠀⠀⠀⢸⣿⣿⢠⣜⡃⠘⣿⣿⡀⠻⣇⠸⣿⣷⠹⡿⣿⣿⠀⠀⠀⠀
                                    ⠀⠘⣿⠀⠀⠀⣠⣿⣿⣿⠸⠋⠀⢠⣿⣿⣧⣀⠀⣠⣿⣿⣧⠃⠘⣿⣧⣄⠀⠀
                                    ⠀⠀⣿⡄⠀⣼⣿⣿⣿⣿⣷⠀⣴⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⣷⣴⣿⣿⣿⣷⠀
                                    ⠀⣠⣿⣷⣄⠘⢛⣋⣽⣾⣷⣤⢘⣽⣾⣷⣷⣶⡎⣽⣶⣶⣯⣯⠁⣫⣿⣯⣩⡀
                                    ⠀⡿⣭⣿⣛⠀⠿⣿⣿⣿⣿⣯⢸⣿⣿⣿⣿⠿⠃⣿⣿⣿⣿⣿⡆⣿⣿⣿⣿⣷
                                    ⠀⣾⣿⣿⣿⡇⠀⠈⢿⣿⣿⡿⠀⢿⣿⣿⡟⠀⢰⣿⣿⣿⠟⢉⣴⣿⣿⣿⡿⠋
                                    ⠀⠈⠛⢿⣿⣧⡀⠀⠸⣿⣿⣇⠀⢸⣿⣿⠃⣰⣿⣿⠟⠁⣠⣿⣿⡿⠋⠁⠀⠀
                                    ⠀⠀⠀⠈⢿⣿⣿⣦⣄⢻⣿⣿⣆⣾⣿⣇⣼⣿⣿⢫⣤⣴⣿⡿⠃⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠹⣿⡿⣟⠸⣿⣿⠟⣿⣛⡛⣽⣿⣿⠸⣿⠟⣿⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠹⡜⣿⡇⣷⣶⣾⣿⣿⣿⣿⡿⢏⣾⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠘⠻⠛⠿⠱⠿⢋⡴⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀
                                     DEDSEC GOOGLE FORM SPAMMER

                                           GITHUB: OXBITX

'''
def nameget():
    name = ["ADRIAN","ALBA","ALBERTO","ALEJANDRO","ALFONSO","ALICIA","ALVARO",
            "ANA","ANDREA","ANDRES","ANGEL","ANGELA","ANTONIA","ANTONIO","BEATRIZ",
            "CARLA","CARLOS","CARMEN","CAROLINA","CLAUDIA","CONCEPCION","CRISTINA",
            "DANIEL","DAVID","DIEGO","DOLORES","EDUARDO","ELENA","ENCARNACION",
            "ENRIQUE","EVA","FERNANDO","FRANCISCA","FRANCISCO","GABRIEL","GUILLERMO",
            "HECTOR","HUGO","IGNACIO","IRENE","ISABEL","IVAN","JAIME","JAVIER","JESUS",
            "JOAQUIN","JORDI","JORGE","JOSE","JOSEFA","JUAN","JUANA","JULIA","LAURA",
            "LUCIA","LUIS","MANUEL","MANUELA","MARC","MARCOS","MARGARITA","MARIA","MARINA",
            "MARIO","MARTA","MERCEDES","MIGUEL","MONICA","MONTSERRAT","NATALIA","NURIA",
            "OSCAR","PABLO","PATRICIA","PAULA","PEDRO","PILAR","RAFAEL","RAMON","RAQUEL",
            "RAUL","RICARDO","ROBERTO","ROCIO","ROSA","ROSARIO","RUBEN","SALVADOR","SANDRA",
            "SANTIAGO","SARA","SERGIO","SILVIA","SOFIA","SONIA","SUSANA","TERESA","VICENTE","VICTOR","YOLANDA",
            'WILLIAM', 'JAMES', 'BENJAMIN', 'HENRY', 'ALEXANDER', 'SAMUEL', 'DANIEL', 'MICHAEL', 'MATTHEW', 'JOSEPH',
            'JOHN', 'DAVID', 'ETHAN', 'LIAM', 'NOAH', 'OLIVER', 'ELIJAH', 'MASON', 'LOGAN', 'LUCAS',
            'AIDEN', 'CARTER', 'JACKSON', 'DYLAN', 'LUKE', 'ANDREW', 'GABRIEL', 'NATHANIEL', 'JONATHAN', 'JACOB',
            'CHRISTOPHER', 'ANTHONY', 'JOSHUA', 'WYATT', 'OWEN', 'LEVI', 'ISAAC', 'JACK', 'NATHAN', 'SAMANTHA',
            'EMMA', 'AVA', 'CHARLOTTE', 'SOPHIA', 'AMELIA', 'ISABELLA', 'MIA', 'HARPER', 'EVELYN', 'ABIGAIL',
            'EMILY', 'ELIZABETH', 'MADISON', 'SCARLETT', 'GRACE', 'CHLOE', 'ZOEY', 'LILY', 'HANNAH', 'LILA',
            'SOFIA', 'VICTORIA', 'AVERY', 'ELEANOR', 'HAZEL', 'NATALIE', 'LUNA', 'ELLA', 'PENELOPE', 'MILY',
            'AURORA', 'RUBY', 'LEAH', 'CORALINE', 'JULIA', 'LUCY', 'LILLIAN', 'AUDREY', 'CLARA', 'ZARA',
            'LEILA', 'CAROLINE', 'AUBREY', 'ALICE', 'VIOLET', 'STELLA', 'ROSE', 'NORA', 'GRACE', 'LEILANI',
            'IVY', 'WILLOW', 'AVALYN', 'ELIANA', 'ISLA', 'ANNABELLE', 'VIVIAN', 'FAITH', 'ELOISE', 'ADELINE',
            'OLIVIA', 'EMMA', 'AVA', 'CHARLOTTE', 'SOPHIA', 'AMELIA', 'ISABELLA', 'MIA', 'HARPER', 'EVELYN',
            'ABIGAIL', 'EMILY', 'ELIZABETH', 'MADISON', 'SCARLETT', 'GRACE', 'CHLOE', 'ZOEY', 'LILY', 'HANNAH',
            'LILA', 'SOFIA', 'VICTORIA', 'AVERY', 'ELEANOR', 'HAZEL', 'NATALIE', 'LUNA', 'ELLA', 'PENELOPE',
            'MILY', 'AURORA', 'RUBY', 'LEAH', 'CORALINE', 'JULIA', 'LUCY', 'LILLIAN', 'AUDREY', 'CLARA',
            'ZARA', 'LEILA', 'CAROLINE', 'AUBREY', 'ALICE', 'VIOLET', 'STELLA', 'ROSE', 'NORA', 'GRACE',
            'LEILANI', 'IVY', 'WILLOW', 'AVALYN', 'ELIANA', 'ISLA', 'ANNABELLE', 'VIVIAN', 'FAITH', 'ELOISE',
            'ADELINE', 'HAILEY', 'NATALIA', 'GENEVIEVE', 'SKYLAR', 'RILEY', 'SAMANTHA', 'KAYLEE', 'SARAH',
            'ALEXIS', 'VANESSA', 'PENNY', 'KATELYN', 'ELIZA', 'MACKENZIE', 'HAYDEN', 'SYDNEY', 'MAYA', 'AALIYAH',
            'KATHERINE', 'NANCY', 'GRACIE', 'BROOKLYN', 'CLAIRE', 'JESSICA', 'EVA', 'ALYSSA', 'ALINA', 'SASHA',
            'MELANIE', 'ALYSSON', 'KAREN', 'AMANDA', 'DAISY', 'TAYLOR', 'REBECCA', 'RACHEL', 'KIMBERLY',
            'JASMINE', 'FIONA', 'VANESSA', 'PAIGE', 'LAUREN', 'CHELSEA', 'ERICA', 'MORGAN', 'LESLIE',
            ]
    
    surnames = [
    'DELA CRUZ', 'GARCIA', 'REYES', 'RAMOS', 'MENDOZA', 'SANTOS', 'FLORES', 'GONZALES', 'BAUTISTA', 'VILLANUEVA',
    'FERNANDEZ', 'CRUZ', 'DE GUZMAN', 'LOPEZ', 'PEREZ', 'CASTILLO', 'FRANCISCO', 'RIVERA', 'AQUINO', 'CASTRO',
    'SANCHEZ', 'TORRES', 'DE LEON', 'DOMINGO', 'MARTINEZ', 'RODRIGUEZ', 'SANTIAGO', 'SORIANO', 'DELOS SANTOS',
    'DIAZ', 'HERNANDEZ', 'TOLENTINO', 'VALDEZ', 'RAMIREZ', 'MORALES', 'MERCADO', 'TAN', 'AGUILAR', 'NAVARRO',
    'MANALO', 'GOMEZ', 'DIZON', 'DEL ROSARIO', 'JAVIER', 'CORPUZ', 'GUTIERREZ', 'SALVADOR', 'VELASCO', 'MIRANDA',
    'DAVID', 'SALAZAR', 'FERRER', 'ALVAREZ', 'SARMIENTO', 'PASCUAL', 'LIM', 'DELOS REYES', 'MARQUEZ', 'JIMENEZ',
    'CORTEZ', 'ANTONIO', 'AGUSTIN', 'ROSALES', 'MANUEL', 'MARIANO', 'EVANGELISTA', 'PINEDA', 'ENRIQUEZ', 'OCAMPO',
    'ALCANTARA', 'PASCUA', 'DE VERA', 'ROMERO', 'DE JESUS', 'DELA PEÑA', 'VALENCIA', 'IGNACIO', 'VERGARA',
    'PADILLA', 'ANGELES', 'ESPIRITU', 'FUENTES', 'LEGASPI', 'CAÑETE', 'PERALTA', 'VARGAS', 'CABRERA', 'FAJARDO',
    'GONZAGA', 'ESPINOSA', 'GUEVARRA', 'SAMSON', 'ORTEGA', 'MOLINA', 'SERRANO', 'CHAVEZ', 'BRIONES', 'MEDINA',
    'PALMA', 'TAMAYO', 'ARELLANO', 'ATIENZA', 'VILLEGAS', 'ESTRADA', 'MARTIN', 'ACOSTA', 'ORTIZ', 'SISON',
    'TRINIDAD', 'ZAMORA', 'ASUNCION', 'ABAD', 'MORENO', 'VALENZUELA', 'MALLARI', 'CABALLERO', 'VILLAMOR',
    'BERNARDO', 'ROBLES', 'CONCEPCION', 'FERNANDO', 'GREGORIO', 'BORJA', 'MAGBANUA', 'DE CASTRO', 'PANGANIBAN',
    'GALANG', 'NUÑEZ', 'ROXAS', 'RUIZ', 'PANGILINAN', 'VICENTE', 'CHUA', 'SUAREZ', 'AVILA', 'ALI', 'AUSTRIA',
    'MAGNO', 'DELA TORRE', 'LUNA', 'DE LA CRUZ', 'PEPITO', 'SOLIS', 'UY', 'DELA ROSA', 'DURAN', 'ABELLA',
    'MAHINAY', 'ESGUERRA', 'ROQUE', 'ANDRES', 'JOSE', 'SEVILLA', 'BELTRAN', 'GABRIEL', 'MATEO', 'YBAÑEZ',
    'NICOLAS', 'MENDEZ', 'CUNANAN', 'VASQUEZ', 'ANCHETA', 'VENTURA', 'LORENZO', 'CORDERO', 'TOLEDO', 'GALVEZ',
    'ABDUL', 'NATIVIDAD', 'MARASIGAN', 'HERRERA', 'SILVA', 'MIGUEL', 'GAMBOA', 'ESTRELLA', 'VILLA', 'BARTOLOME',
    'USMAN', 'SALES', 'CUSTODIO', 'ONG', 'LUCERO', 'ABDULLAH', 'MANZANO', 'IBAÑEZ', 'MARCELO', 'PONCE',
    'GALLARDO', 'ROSARIO', 'DELGADO', 'CANLAS', 'CARIÑO', 'YAP', 'GO', 'ESTEBAN', 'ILAGAN', 'TUAZON', 'CARPIO',
    'CARREON', 'BALTAZAR', 'PABLO', 'LOZADA', 'GUZMAN', 'GUERRERO', 'PADUA', 'SALCEDO', 'CAMACHO', 'SAN JUAN',
    'BUENO', 'BLANCO', 'CUEVAS', 'CARLOS', 'ANDAYA', 'LOZANO', 'AGUIRRE', 'BAGUIO', 'CERVANTES', 'BERNAL',
    'BUSTAMANTE', 'AREVALO', 'VILLAR', 'SABADO', 'LABRADOR', 'RONQUILLO', 'PANES', 'CRISTOBAL', 'PRADO',
    'GUILLERMO', 'DULAY', 'APOSTOL', 'OLIVEROS', 'SANTILLAN', 'ABALOS', 'QUINTO', 'MONTERO', 'ALFONSO', 'UMALI',
    'CAMPOS', 'CONSTANTINO', 'BAYLON', 'MALINAO', 'FRANCO', 'CALDERON', 'QUIJANO', 'VELASQUEZ', 'MARCOS',
    'ALONZO', 'LAZARO', 'MATA', 'CINCO', 'GERONIMO', 'CORDOVA', 'EUGENIO', 'RUBIO', 'VIRAY', 'DELFIN', 'CANOY',
    'CRISOSTOMO', 'MEJIA', 'RICO', 'PUNZALAN', 'BENITEZ', 'BERNABE', 'BUENAVENTURA', 'BALLESTEROS', 'CLEMENTE',
    'SY', 'PEÑA', 'JACINTO', 'VIDAL', 'SALAS', 'TOMAS', 'MATIAS', 'YU', 'DE ASIS', 'ANDRADE', 'MAGALLANES',
    'ROLDAN', 'ASIS', 'LEDESMA', 'CORTES', 'FELICIANO', 'SAYSON', 'DE LUNA', 'BORROMEO', 'DEL MUNDO', 'BELLO',
    'MANANSALA', 'BONDOC', 'LACSON', 'SALINAS', 'BARRIENTOS', 'CONDE', 'COLLADO', 'JUAN', 'VILLAREAL', 'TEVES',
    'LAURENTE', 'QUIAMBAO', 'MOHAMMAD', 'OLIVA', 'BONIFACIO', 'ROJAS', 'ALEJANDRO', 'SEBASTIAN', 'FRIAS', 'CATALAN',
    'ESPINA', 'LEE', 'LUCAS', 'SALI', 'DOMINGUEZ', 'MANGUBAT', 'CALMA', 'CHAN', 'VILLARIN', 'CAYABYAB', 'ROSAL',
    'BASA', 'BASILIO', 'TEJADA', 'SAMONTE', 'VIERNES', 'PLAZA', 'GALLEGO', 'CASTOR', 'DIONISIO', 'MUSA',
    'SULTAN', 'TENORIO', 'SOLOMON', 'ESPAÑOLA', 'NARCISO', 'SAN JOSE', 'PANGAN', 'PELAYO', 'ROMANO', 'LACHICA',
    'ARCILLA', 'ALBA', 'ESPINO', 'RAYMUNDO', 'PILAPIL', 'CUIZON', 'ARAGON', 'MEDRANO', 'ANG', 'GUINTO', 'CASTAÑEDA',
    'PARAS', 'ALVARADO', 'OMAR', 'HIPOLITO', 'PORRAS', 'DE MESA', 'TECSON', 'BASCO', 'PIMENTEL', 'ADRIANO',
    'SANTA ANA', 'SAGUN', 'PACHECO', 'MUÑOZ', 'LANDICHO', 'ARROYO', 'RODRIGO', 'NERI', 'MALABANAN', 'BRAVO',
    'LARA', 'DELA CERNA', 'VILLAFLOR', 'GALICIA', 'JUNIO', 'DE LOS SANTOS', 'VILLARUEL', 'HILARIO', 'AÑONUEVO',
    'FELIPE', 'MONTES', 'GASPAR', 'BELEN', 'SOTTO', 'PATRICIO', 'BERNARDINO', 'MADRID', 'ALARCON', 'VERANO',
    'CASAS', 'BARRIOS', 'ARIOLA', 'CANO', 'ADVINCULA', 'MARCELINO', 'MACARAEG', 'ALEJO', 'ANDAL', 'DALISAY',
    'AGUILA', 'LAO', 'SUNGA', 'DE CHAVEZ', 'MONTEMAYOR', 'CORONEL', 'SILVESTRE', 'CARILLO', 'BERMUDEZ', 'ZAPANTA',
    'CO', 'MURILLO', 'BILLONES', 'BELARMINO', 'DIMAANO', 'MAHILUM', 'ALEGRE', 'NEPOMUCENO', 'DE OCAMPO', 'ALBERTO',
    'ABAS', 'MANLANGIT', 'VEGA', 'MANALANG', 'LIWANAG', 'PAGLINAWAN', 'MENESES', 'IBRAHIM', 'AGUINALDO', 'BACANI',
    'HASSAN', 'CARIAGA', 'BURGOS', 'MARANAN', 'RECTO', 'VILLAFUERTE', 'IMPERIAL', 'SAN PEDRO', 'MANABAT', 'ZABALA',
    'FIGUEROA', 'AMANTE', 'PAZ', 'SANDOVAL', 'DELIMA', 'URBANO', 'QUIÑONES', 'DECENA', 'DE VILLA', 'SALONGA',
    'ANDRADA', 'POLICARPIO', 'PASION', 'ROA', 'CAPISTRANO', 'CABAHUG', 'CARANDANG', 'MADRIAGA', 'ISMAEL',
    'SAAVEDRA', 'MAMA', 'DELA VEGA', 'JULIAN', 'DE LOS REYES', 'PANCHO', 'NOLASCO', 'JACOB', 'FONTANILLA',
    'TOBIAS', 'BENITO', 'DONATO', 'BACUS', 'MAGSINO', 'VALERIO', 'DY', 'RIVAS', 'PARAISO', 'VILORIA', 'PAREDES',
    'SOLANO', 'JUMAWAN', 'REGALA', 'VILLENA', 'ROJO', 'MAGPANTAY', 'ARCEO', 'MINA', 'FLORENDO', 'CENTENO',
    'ENCARNACION', 'MENDIOLA', 'REGALADO', 'BALUYOT', 'MOJICA', 'MAYO', 'ACUÑA', 'ALFARO', 'DE TORRES', 'GATCHALIAN',
    'MAHUSAY', 'SORIA', 'OSORIO', 'ARANETA', 'DIVINAGRACIA', 'MONTAÑO', 'BARREDO', 'SUMALINOG', 'AKMAD', 'LARGO',
    'LAURON', 'SIMON', 'SABANAL', 'HIDALGO', 'BARRERA', 'VALIENTE', 'MACAPAGAL', 'BARCELONA', 'ISIDRO', 'BACALSO',
    'RAFAEL', 'LOYOLA', 'RESURRECCION', 'SANTA MARIA', 'RAZON', 'CAPILI', 'FELIX', 'VELARDE', 'TEODORO', 'BERNALES',
    'INFANTE', 'NAVALES', 'DORADO', 'YABUT', 'DUQUE', 'CABALLES', 'BENEDICTO', 'PASTOR', 'ABUBAKAR', 'MONDEJAR',
    'FAUSTINO', 'PASCO', 'ESTACIO', 'HERMOSO', 'LAZO', 'BUENAFLOR', 'DANAO', 'PEÑAFLOR', 'MESA', 'BANTILAN',
    'MARZAN', 'DAYRIT', 'BOHOL', 'CATACUTAN', 'PAGADUAN', 'PALACIO', 'BELLEZA', 'DACANAY', 'MAGNAYE', 'PEÑARANDA',
    'ARGUELLES', 'ALMAZAN', 'PAMINTUAN', 'CANDELARIA', 'INOCENCIO', 'MACATANGAY', 'MORILLO', 'LAPUZ', 'PALMES',
    'SARIP', 'AMIL', 'SUAN', 'BORRES', 'SULIT', 'TADEO', 'MAGAT', 'PADERNAL', 'DUMLAO', 'BALBUENA', 'VILLAROSA',
    'GUANZON', 'PARREÑO', 'PUNO', 'REVILLA', 'CARDENAS', 'PAULINO', 'MIJARES', 'PANALIGAN', 'ALIH', 'MANLAPAZ',
    'CABRAL', 'MANALILI', 'MARAVILLA', 'AMPUAN', 'LLAGAS', 'ARENAS', 'PARCON', 'LEONARDO', 'ALCALA', 'BERMEJO',
    'BUENAFE', 'SANGALANG', 'GALLO', 'DIEGO', 'FABIAN', 'COSTALES', 'SOLIMAN', 'JORDAN', 'DE GUIA', 'SALVA',
    'TAYAG', 'COMIA', 'AMOR', 'JAYME', 'ROSETE', 'CUARESMA', 'NAZARENO', 'ABAYON', 'PASTRANA', 'MAGLASANG',
    'TUPAS', 'CATAPANG', 'ADAM', 'BELMONTE', 'CAYETANO', 'MAMARIL', 'CACHO', 'DUEÑAS', 'FLORENTINO', 'SAN DIEGO',
    'BARRAMEDA', 'POBLETE', 'PAPA', 'REAL', 'LAXAMANA', 'ABARQUEZ', 'CADIZ', 'AMPARO', 'SINGSON', 'CUETO',
    'DELA PAZ', 'MORAL', 'ABAO', 'BANAAG', 'MONTOYA', 'PITOGO', 'CAMPO', 'VALLE', 'GLORIA', 'CUENCA', 'SALIK',
    'EUSEBIO', 'BULAN', 'AMPASO', 'ARIAS', 'REY', 'VICTORIA', 'GRANADA', 'PAMA', 'ALMONTE', 'CELIS', 'MALATE',
    'ALMARIO', 'BALINGIT', 'OLIVAR', 'JOAQUIN', 'TAGALOG', 'SIBAYAN', 'CONTRERAS', 'MONTEJO', 'PALOMO', 'LAGMAN',
    'QUIZON', 'APOLINARIO', 'PARAGAS', 'GAVIOLA', 'DAYAO', 'ANDALES', 'SILVANO', 'MONTILLA', 'ESTRERA', 'ABAN',
    'ALCARAZ', 'FRONDA', 'IBARRA', 'MORADA', 'DIAMANTE', 'NAVAL', 'PULIDO', 'BALANSAG', 'ROSAS', 'MARIÑAS',
    'CORNELIO', 'BAÑEZ', 'PALOMAR', 'ADOLFO', 'AMARO', 'RENDON', 'SANICO', 'VALERA', 'BUAN', 'AMORES', 'CARO',
    'CASTILLON', 'MORA', 'ANDO', 'BARON', 'CORONADO', 'BALMES', 'NACARIO', 'DATU', 'GOROSPE', 'SIMBAJON',
    'PANTALEON', 'DE LARA', 'CENIZA', 'OLARTE', 'SAMILLANO', 'TORIO', 'RAMA', 'ESCALANTE', 'TAGLE', 'CLARO',
    'ESCOBAR', 'AVENIDO', 'RABINO', 'SALVACION', 'PELAEZ', 'YUMUL', 'LEAL', 'AMAR', 'GERONA', 'NAVA', 'ZULUETA',
    'TAMPUS', 'ALFEREZ', 'ARANAS', 'GALVAN', 'FRANCIA', 'AGCAOILI', 'MIRASOL', 'KASIM', 'NACION', 'POSADAS',
    'CANILLO', 'DE DIOS', 'ESTABILLO', 'GUMBAN', 'BUENA', 'APOSTOL', 'ALCANTARA', 'CASASOLA', 'MATUTE', 'BRIZ',
    'VALLEJO', 'LACANLALE', 'GONZALVO', 'LOMA', 'GARBANZO', 'LABAN', 'VICENTILLO', 'FERRIOL', 'ADRIATICO',
    'EUSTAQUIO', 'SABILE', 'DE GUZMAN', 'LAPENA', 'IBARRIENTOS', 'OLIVO', 'APUAN', 'DADO', 'SARSALEJO',
    'ANDALES', 'DALEON', 'LAGUNERO', 'PETILLA', 'ARROZ', 'ISIDRO', 'LEPITEN', 'BAGGAY', 'NAVARRETE', 'ROJAS',
    'ALFECHE', 'SIMONDS', 'MANSUETO', 'OREIRO', 'EMPLEO', 'GALES', 'MENDIOLA', 'MANINGAS', 'FLORESCA',
    'SALONGA', 'MANALAYSAY', 'VALMORIA', 'SINENSE', 'PAGALAN', 'SAJULGA', 'PORRAS', 'TORDECILLA', 'NAVARRO',
    'SIPIN', 'CAISIP', 'ESMERO', 'AVILES', 'JOBO', 'MONATO', 'MILITANTE', 'ALFORNON', 'BAUZON', 'RAZOTE',
    'AGGABAO', 'ESPIRITU', 'DELOS SANTOS', 'RAGONOT', 'APOSTOL', 'BAHILLO', 'SALDAÑA', 'QUIÑO', 'AGBAYANI',
    'GATDULA', 'FAMILARA', 'LEONG', 'HERNAN', 'ABELLANOSA', 'OABEL', 'CANCINO', 'RUPAC', 'DACUA', 'LIPATA',
    'TOLEDO', 'RIVANO', 'CAMPOSANO', 'STO DOMINGO', 'CATAAG', 'BARIA', 'GENITA', 'DELA CRUZ', 'BALLESTA',
    'ALINSUNURIN', 'TALINGTING', 'NAPIÑAS', 'CIRUJANO', 'MASCARDO', 'RAMIRO', 'BARRANDA', 'CORALDE', 'BAGUNU',
    'SALAZAR', 'DAVID', 'ACERO', 'BOLANIO', 'CALICA', 'GUECO', 'RAGOT', 'BESIN', 'COLIGADO', 'ROSQUITA',
    'TABIAN', 'BALEÑA', 'BORDADORA', 'MENDOZA', 'NOSAL', 'CRUZ', 'CORBILLON', 'DAGDAG', 'CUYUGAN', 'SACLAG',
    'RACAL', 'JARANILLA', 'DELGADO', 'CABRILLOS', 'QUEZON', 'ABENIDO', 'LEDESMA', 'BAHAG', 'NAPIGKIT',
    'CORTEZ', 'DELA TORRE', 'BARZAGA', 'SALEN', 'ALCAYAGA', 'LABAGALA', 'BILANGLO', 'PINEDA', 'BENEDICTO',
    'FLORIA', 'RONQUILLO', 'VALMEO', 'DEL CAMPO', 'CATACUTAN', 'ZABALA', 'BAÑAS', 'HINAUT', 'DELGADO',
    'OROSCO', 'DELFIN', 'DE LEON', 'CERIALES', 'LAZARO', 'DOCTO', 'VILLAVICENCIO', 'BARROGA', 'VERALLO',
    'BANAS', 'MACAPAGAL', 'HOMENA', 'PASCUA', 'ROSANA', 'SAMANIEGO', 'TABUJARA', 'VILLAPAZ', 'LAPUZ',
    'MAGALLON', 'ROJO', 'QUIRIMIT', 'RESURRECCION', 'ABALOS', 'JAVATE', 'NOEL', 'BASCO', 'PIMENTEL', 'POLICARPIO',
    'AMOR', 'NATIVIDAD', 'BRIONES', 'MAMAYSONG', 'CARREON', 'JASMIN', 'MACARAIG', 'VALENCIA', 'BARRAMEDA',
    'BUAN', 'PALOMARES', 'MAMANGON', 'RODIL', 'RIVERA', 'ESTORES', 'DEL CASTILLO', 'QUIJANO', 'PENASO',
    'ARCIGA', 'LACSA', 'BEBIS', 'BALAO', 'JAVIER', 'CARMELO', 'CASTILLO', 'MAMARIL', 'TUANO', 'GARCIA',
    'GABIOLA', 'SALANGSANG', 'ALBACITE', 'LUCENA', 'BATTUNG', 'SAMONTE', 'LONTOC', 'CAPUNO', 'CASTRO',
    'MACABILANG', 'BADILLO', 'ROSARIO', 'GABOR', 'CUERVO', 'ATIENZA', 'ARREOLA', 'CAMAT', 'LABITA', 'BULAGA',
    'ALMANZA', 'TUVERA', 'RAJAH', 'NAVARRO', 'ILANO', 'BATULA', 'CULALA', 'ORTEGA', 'SIBAYAN', 'LEAL',
    'SALAVANTE', 'LANTO', 'BADAR', 'QUEVADA', 'DELA CRUZ', 'SAMBAYON', 'MORALES', 'ALO', 'JANABAN', 'CARREON',
    'COSCA', 'CAHAYAG', 'JARDIN', 'MALLARI', 'BELARMINO', 'HERNANDO', 'SALVACION', 'MALBAS', 'BOJOS', 'HERNANDEZ',
    'PANGANIBAN', 'JUMAWAN', 'VALLES', 'GADIA', 'NAVALTA', 'PANELO', 'DEVERO', 'SACRO', 'SUZARA', 'TAÑAMOR',
    'PINEDA', 'TUVIDA', 'AMORA', 'MALONZO', 'SALIDO', 'SULAIMAN', 'CABANES', 'CAMACHO', 'BRILLO', 'LAGAT',
    'EUGENIO', 'REYES', 'VIRAY', 'DEL ROSARIO', 'PAGSOLINGAN', 'GUINA', 'NATIVIDAD', 'MABINI', 'QUISTO',
    'DACOCO', 'LOPEZ', 'MARAMAG', 'LLENA', 'NAPULI', 'CORNEJO', 'CERVANTES', 'PULGAR', 'SINAG', 'CABOTAGE',
    'SAUZA', 'PILLADO', 'AMISTAD', 'VICENTE', 'RIO', 'MANUEL', 'HERMOGENES', 'BULOTANO', 'DE LA CRUZ',
    'SALES', 'OROZCO', 'NABUA', 'LAPID', 'SAMARITA', 'GRANIL', 'LUCERO', 'BELMONTE', 'MONZON', 'HERMOSISIMA',
    'BEREDO', 'MIRANDA', 'UMALI', 'TUALLA', 'MONJE', 'BALDERAS', 'AGUILAR', 'PALCON', 'NAVALES', 'FANTONALGO',
    'DELFIN', 'FLORIA', 'PERADILLA', 'LALU', 'CAHULOGAN', 'MAHIPUS', 'LAUDE', 'PASCUA', 'APOSTOL', 'ARIAS',
    'DEL PRADO', 'TURLA', 'LAURENTE', 'NACU', 'ESMAN', 'SERRANO', 'ALMOGUERA', 'ZAPANTA', 'MELENDRES',
    'GREGORIO', 'SULAPAS', 'DE CASTRO', 'NOCHE', 'PASTRANO', 'ELISAN', 'CALIBO', 'BAULA', 'MORALEDA',
    'ANDRADA', 'BERINO', 'HERMO', 'BAYANI', 'BELMONTE', 'TUGADE', 'MONTEMAYOR', 'DELA CRUZ', 'PIÑON',
    'BUENA', 'CALINGASAN', 'CUI', 'PILI', 'MANZANO', 'DE MESA', 'GERMO', 'AÑONUEVO', 'RUBIO', 'FLORENDO',
    'DE PERALTA', 'SAN PEDRO', 'MENDEZ', 'JAVIER', 'MILITAR', 'CAMINERO', 'YUMUL', 'ANOR', 'MACALINTAL',
    'MAGBITANG', 'TIAMSON', 'CERIA', 'ANDRADE', 'DUPAYA', 'BANATANTO', 'NOBLE', 'VISTA', 'VILLANUEVA',
    'VICENTE', 'MERCADO', 'MERENCILLA', 'PANUNCIO', 'FERRIOL', 'MERZA', 'BADANA', 'BRUAL', 'PEPE', 'VELASQUEZ',
    'FERMIN', 'ALVARADO', 'NITURA', 'PARANE', 'LAVILLA', 'HIZON', 'LUCILA', 'TUAZON', 'SERAFICA', 'CUMBA',
    'ALIPIO', 'VEGAS', 'HERNANDO', 'MERCURIO', 'MONDELO', 'ABADIA', 'TOLEDO', 'TOMINES', 'MANLANGIT', 'VILLALUNA',
    'CALIVO', 'REBUCAS', 'DANCEL', 'CANO', 'HERNAN', 'ROSETE', 'LUPO', 'SALIDO', 'REMA', 'CAÑAS', 'DELEÑA',
    'MATABANG', 'ELEAZAR', 'BATUNGBACAL', 'LUMAPAS', 'SAYLO', 'CONCEPCION', 'EUFEMIO', 'POBLETE', 'FERRER',
    'PONFERRADA', 'MARCAIDA', 'CHUA', 'MAZON', 'SACLOLO', 'ELERA', 'FLORES', 'CAPULOT', 'EUSORES', 'DEL MONTE',
    'CUARESMA', 'ANDRION', 'DIMAANO', 'ERICE', 'LIRIO', 'DALEN', 'SALONGA', 'VELLOSO', 'VALLARTA', 'SORIANO',
    'MALANG', 'ARCILLA', 'TAMBIS', 'RESUELLO', 'MERCADO', 'TUGNA', 'ELNAR', 'SILVESTRE', 'CLARO', 'CONCIO',
    'TEVES', 'VILLAROSA', 'NEBRES', 'ESPULGAR', 'CAMPUSANO', 'CONCHA', 'PANDAY', 'DORIA', 'ALCANTARA',
    'PEÑALOZA', 'DIWA', 'REBOQUIO', 'CORRO', 'VILLA', 'GARCIA', 'ROSEL', 'DELICA', 'AGTARAP', 'FLOR',
    'REVELAR', 'PALMA', 'POLIQUIT', 'LIGGAYU', 'AMOGUIS', 'MENDAVIA', 'BEÑAS', 'TALEON', 'DIZON', 'CAVITE',
    'ABAG', 'ALFEREZ', 'VILLARUEL', 'TIAPE', 'MABASA', 'GALANG', 'MERCURIO', 'ARENAS', 'GERERO', 'LOMAS',
    'MOJADO', 'POBLETE', 'DE LEON', 'BONAVENTURA', 'SOMERA', 'ROSIMA', 'PANDA', 'MORABE', 'CALINGASAN',
    'SIA', 'ANGULO', 'MIJARES', 'BORBON', 'CAÑEDO', 'BAGANG', 'JACOB', 'MONTILLA', 'SAN JOSE', 'GERONIMO',
    'RIVERA', 'BUADO', 'DUMANGENG', 'TINIO', 'ESPINA', 'SIMANGAN', 'BALLESTEROS', 'SALAZAR', 'AROMIN', 'BALDO',
    'ALON', 'MANATAD', 'SAYAT', 'SALAMAT', 'NUEVA', 'CAMARA', 'MALUPENG', 'LANTICAN', 'CASIÑO', 'ANGWAY',
    'DAGANDAN', 'NACAR', 'BOLANOS', 'PALOMO', 'CANDIA', 'APOSTOL', 'DINO', 'DIMASANGKAY', 'LAGUMBAY',
    'BUCALBOS', 'MAMUYAC', 'MACARAIG', 'MATIAS', 'ALVIAR', 'CINCO', 'PINEDA', 'BOBIS', 'BORJAL', 'DACUMOS',
    'FLORANDA', 'GERMINO', 'OCUMEN', 'SUSAYA', 'PADUA', 'TOMAWIS', 'TUBAN', 'VELORIA', 'MINA', 'DIONES',
    'TUAZON', 'ELMIDO', 'PAGARIGAN', 'CHUA', 'PETILLA', 'GILLESANIA', 'SOLOMON', 'MAHIPUS', 'DUMAS', 'BRUA',
    'MAHAL', 'MENDINA', 'DEL ROSARIO', 'OCAY', 'JAVIER', 'SALDIVAR', 'ELEFAN', 'DAVID', 'BOLANOS', 'VALMORES',
    'GAJO', 'ANGLUBEN', 'ARO', 'CANDADO', 'PADER', 'CORPIN', 'SOLOMON', 'SULAPAS', 'CUBIO', 'REGALADO',
    'CASINTO', 'PADILLA', 'BUENO', 'MAHUMOT', 'BORDADO', 'LAPUZ', 'DIOCSON', 'CASCARA', 'LUCIO', 'CATAPANG',
    'ADARLO', 'NANO', 'SARCAUGA', 'QUEZON', 'GUEVARRA', 'NAVA', 'LAUZON', 'ESMIQUE', 'ABRAHANO', 'SALAS',
    'MALLILLIN', 'LONTOC', 'ALPAY', 'TUAZON', 'RUBI', 'BALITA', 'DELEÑA', 'ALCUZAR', 'ASERON', 'JORDAN',
    'ROGEL', 'LACOSTE', 'DAVID', 'CALUB', 'MACALALAD', 'MACALINO', 'TUAZON', 'AREVALO', 'BAUTISTA', 'BALOR',
    'SALVACION', 'LUNA', 'SALAZAR', 'DALIDA', 'DAYAO', 'ROSAL', 'MACALINO', 'SAMANIEGO', 'GONZALES',
    'DALIDA', 'ALFORTE', 'BUENDIA', 'CASCARA', 'MACABANGKIT', 'CALAGOS', 'LAGUMBAY', 'CASAL', 'BONDOC',
    'PETILLA', 'SIBUG', 'SALAZAR', 'DIOCSON', 'ACOSTA', 'CINCO', 'ACUÑA', 'MATIAS', 'DINO', 'MARAMAG',
    'DAYAO', 'PALOMA', 'ANZURES', 'MACALALAD', 'CASCARA', 'MEJIA', 'CABALAN', 'ALIP', 'BALAG', 'DACUMOS',
    'ESTRELLA', 'LONTOC', 'BALITA', 'ARQUIZA', 'JOSE', 'ALCAIDE', 'SALVACION', 'CACERES', 'ROSAL', 'LOPEZ',
    'MALOLOY-ON', 'PALOMA', 'SIBUG', 'DE LA CRUZ', 'CACERES', 'SERRANO', 'BILAGANTOL', 'ALBIOS', 'ANZURES',
    'ESTRELLA', 'JORDAN', 'MEJIA', 'MACALINO', 'SERRANO', 'MACALALAD', 'LAGUMBAY', 'CABALAN', 'SALVACION',
    'SALAZAR', 'ARQUIZA', 'ROSAL', 'DAYAO', 'DE LA CRUZ', 'LONTOC', 'PALOMA', 'CACERES', 'MALOLOY-ON', 'DINO',
    'CACERES', 'DE LA CRUZ', 'SERRANO', 'MACALALAD', 'LAGUMBAY', 'SALVACION', 'SALAZAR', 'BALITA', 'PALOMA',
    'LONTOC', 'MALOLOY-ON', 'DAYAO', 'CACERES', 'DINO', 'ARQUIZA', 'ROSAL', 'CACERES', 'DE LA CRUZ',
    'SALVACION', 'MACALALAD', 'MEJIA', 'MACALINO', 'LAGUMBAY', 'SALAZAR', 'LONTOC', 'PALOMA', 'BALITA', 'DINO',
    'MALOLOY-ON', 'ARQUIZA', 'CACERES', 'DE LA CRUZ', 'SERRANO', 'SALVACION', 'SALAZAR', 'MEJIA', 'LAGUMBAY',
    'MACALALAD', 'PALOMA', 'DINO', 'MALOLOY-ON', 'CACERES', 'ROSAL', 'SALAZAR', 'MEJIA', 'MACALINO', 'ARQUIZA',
    'LAGUMBAY', 'DINO', 'SALAZAR', 'MACALALAD', 'PALOMA', 'CACERES', 'ROSAL', 'MALOLOY-ON', 'LAGUMBAY',
    'MACALALAD', 'MEJIA', 'SALAZAR', 'ARQUIZA', 'PALOMA', 'DINO', 'MALOLOY-ON', 'CACERES', 'LAGUMBAY',
    'MACALALAD', 'ROSAL', 'SALAZAR', 'PALOMA', 'ARQUIZA', 'DINO', 'MEJIA', 'MALOLOY-ON', 'SALAZAR',
    'CACERES', 'ROSAL', 'ARQUIZA', 'PALOMA', 'MEJIA', 'SALAZAR', 'LAGUMBAY', 'DINO', 'ARQUIZA', 'PALOMA',
    'CACERES']

    last1 = list(surnames)
    return name[random.randint(0, len(name)-1)],last1[random.randint(0, len(last1)-1)]

def mailget(name, last_name):
    last_no_space = last_name.replace(' ', '') or last_name.replace('  ', '')

    random_digits = ''.join(random.choice('0123456789') for _ in range(3))
    mail = ["gmail.com", "hotmail.com", "protonmail.com", "outook.com", "yahoo.com"]
    
    return (name + last_no_space + random_digits + "@" + random.choice(mail)).lower()

def phone_num_get():
    random_digits = ''.join(random.choice('0123456789') for _ in range(9))
    phnum = '09' + random_digits
    return phnum

def bdayget():
    number = ""
    number = number + str(random.randint(1, 31))
    if int(number) < 10:
        number = "0" + str(number)
    number = number + "/"
    number = number + str(random.randint(1, 12))
    if int(number[3:]) < 10:
        number = str(number[:3]) + "0" + str(number[3:])
    if int(number[:2]) > 28 and int(number[3:]) == 2:
        number = number[:2] + "28" + number[4:]
    number = number + "/"
    x = datetime.datetime.now()
    year = (x.strftime("%Y"))
    year1 = int(year) - 60
    year2 = int(year) - 20
    birth_year = random.randint(year1, year2)
    number = number + str(birth_year)
    age = int(year) - birth_year

    return number, age

def city_get():
    philippine_cities = [
    "Quezon City",
    "Manila",
    "Caloocan",
    "Budta",
    "Davao City",
    "Malingao",
    "General Santos",
    "Taguig",
    "Pasig",
    "Antipolo",
    "Cagayan de Oro",
    "Parañaque",
    "Zamboanga City",
    "Valenzuela",
    "Las Piñas",
    "Makati",
    "Bacolod City",
    "Mansilingan",
    "Cebu",
    "Mandaue City",
    "Iloilo City",
    "Pasay",
    "San Jose del Monte",
    "Bacoor",
    "Iligan City",
    "Cabuyao",
    "Calamba",
    "Meycauayan",
    "Marikina",
    "Navotas",
    "Dasmariñas",
    "Muntinlupa",
    "San Fernando",
    "Lapu-Lapu City",
    "Olongapo",
    "San Pablo",
    "Malolos",
    "Lipa",
    "Biñan",
    "Palo",
    "Batangas",
    "Los Baños",
    "Naga",
    "Cotabato City",
    "Dagupan",
    "Toledo",
    "Legaspi",
    "Lucena",
    "Tarlac City",
    "Santiago",
    "Tuguegarao City",
    "Cavite City",
    "Ozamiz City",
    "Ormoc",
    "Calbayog City",
    "Kabankalan",
    "Cabanatuan",
    "Surigao",
    "Dipolog",
    "Talisay",
    "Valencia",
    "Kidapawan"
    "Malaybalay",
    "Pagadian",
    "Tabuk",
    "Digos",
    "San Carlos",
    "Gingoog",
    "Baliuag",
    "San Mateo",
    "Panabo",
    "Koronadal",
    "Libertad",
    "Male",
    "Alabel",
    "Bayawan",
    "Silay",
    "Sexmoan",
    "Gapan",
    "Sorsogon",
    "Tanza",
    "Roxas City",
    "Laoag",
    "Calapan",
    "Kabacan",
    "Sagay",
    "Alaminos",
    "Carcar",
    "La Carlota",
    "Tagbilaran",
    "Iriga",
    "Bislig",
    "Muñoz",
    "Surallah",
    "Malita",
    "Sipalay",
    "Cabagan",
    "Abuyog",
    "Bontoc",
    "Hinigaran",
    "Dumaguete",
    "Candon",
    "Bayugan",
    "Virac",
    "Tabaco",
    "Masbate",
    "Bayambang",
    "Solano",
    "Banga",
    "Laoang",
    "Arayat",
    "Capas",
    "Amadeo",
    "Bay",
    "Sultan Kudarat",
    "Jose Panganiban",
    "Santa Cruz",
    "Aparri",
    "Bongao",
    "Catbalogan",
    "Mati",
    "San Ildefonso",
    "San Vicente",
    "Alicia",
    "Kalibo",
    "Tanauan",
    "Pagbilao",
    "Santa Maria",
    "Digos",
    "Cordova",
    "Bislig",
    "Maramag",
    "Cabiao",
    "Taytay",
    "Tagoloan",
    "Kabugao",
    "Candelaria",
    "Bugo",
    "Veruela",
    "Batac",
    "Polomolok",
    "Baliuag",
    "Malaybalay",
    "La Castellana",
    "Lubao",
    "Tabuk",
    "Tagas",
    "Balanga",
    "Malungun",
    "Narra",
    "Cabadbaran",]
    return philippine_cities[random.randint(0, len(philippine_cities)-1)]

def getid(length=24):
    characters = string.digits + string.ascii_lowercase
    random_id = ''.join(random.choices(characters, k=length))
    return random_id

random_id = getid()

def runme():
    print(banner)

    try:
        while True:
            random_digits = ''.join(random.choice('0123456789') for _ in range(3))
            name,last_name = nameget() 

            firstname = name.lower()
            lastname  = last_name.lower() 
            phone_number = phone_num_get()
            birthday, age = bdayget()
            address = city_get()
            password = firstname + lastname + random_digits
            email = mailget(name,last_name)

            url = "https://docs.google.com/forms/d/e/1FAIpQLSdDXxjytZnmjwOEeMK8PjSJG-shr0UKNPg5nm7dknFi4wGDDg/formResponse"

            headers = {
                "Cookie": "S=spreadsheet_forms=wfdh4NG44Qt2hwbdd8gKy1HHOF2JPQg-T4IlJA9hMEA; COMPASS=spreadsheet_forms=CjIACWuJVzg5xsF0brWfqA0JdroOU1plgvuvL4bvFI6-Q3YX-v7V8o7ZusjHzUb6dfu8-hDQjumqBho0AAlriVezLLHdW7G10dfxpbZXAbZpnIqBnw0OH7Xk-mDbbWo89mJsB0MYxxLv3wS8jPGRoQ==; NID=511=N4043kekB5EkZRRpKKnGx3VpeA2i1-V47i8_3QABGrmdIDIp7Z9MebmM_PcAktcn4S7cjHHbNiuueB683ETlWTb0CAdVFGfARsi-Bvob0n0Ksa6MPCXNhJwEGauWpdXi3hEwHyXqhuPsdDk0KdMGeBC7AE3fNhgmNWe0aNMfFjg",
                "Host": "docs.google.com",
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Content-Type': 'application/x-www-form-urlencoded',
                "Origin": "https://docs.google.com",
                "Referer": "https://docs.google.com/forms/d/e/1FAIpQLSdDXxjytZnmjwOEeMK8PjSJG-shr0UKNPg5nm7dknFi4wGDDg/viewform?fbzx=-3065528922530206851",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
                "X-Client-Data": "CKblygE=",
                'Upgrade-Insecure-Requests':'1'
            }

            body = {
                'entry.1630406277': email,
                'entry.254235199': password,
                'entry.17821565': firstname + ' ' + lastname,
                'entry.699087705': address,
                'entry.509920065': phone_number,
                'fvv': '1',
                'partialResponse': '[null,null,"-3065528922530206851"]',
                'pageHistory': '0',
                'fbzx': '-3065528922530206851'
            }

            response = requests.post(url, headers=headers, data=body)

            attack = f"[*] firstname: \033[92m{firstname.ljust(13)}\033[0m lastname: \033[92m{lastname.ljust(15)}\033[0m age: \033[92m{str(age).ljust(4)}\033[0m birthday: \033[92m{birthday.ljust(11)}\033[0m phone_number: \033[92m{phone_number.ljust(13)}\033[0m address: \033[92m{address.ljust(15)}\033[0m email: \033[92m{email.ljust(35)}\033[0m password: \033[92m{password.ljust(20)}\033[0m status: \033[92m{response.status_code}\033[0m "
            print(attack)
    
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    thread = threading.Thread(target=runme)
    thread.start()