# PROGRAMA PARA A IDENTIFICAÇÃO DE SISTEMAS PELO MÉTODO DOS MÍNIMOS QUADRADOS
# AUTOR: LUCAS BOARIM PALUDO

#pacotes utilizados
from mat4py import loadmat
import numpy as np
from control.matlab import *
import matplotlib.pyplot as plt

#entrada com o número de polos e zeros desejado no sistema
num_polos = int(input('\033[32mDigite o número de polos desejado:\033[m '))
num_zeros = int(input('\033[32mDigite o número de zeros desejado:\033[m '))

#verifica condição para o sistema ser estável
while num_zeros > num_polos:
     print('''
     \033[31mOpção inválida!\033[m
     \033[33mPara que o sistema seja estável o número de polos deve ser igual ou maior que o número de zeros.\033[m''')
     num_zeros = int(input('\n\033[32mDigite o número de zeros desejado:\033[m '))
     if num_zeros <= num_polos:
          break
     else:
          continue

#entrada com o número de amostras coletadas
num_amostras = int(input('\033[32mDigite o número de amostras:\033[m '))

#cria vetores para manipulação da matriz de regressores
vetor_sub_polos = np.arange(1, num_polos+1)
vetor_sub_zeros = np.arange(0, num_zeros+1)

#lê os dados de identificação do Matlab e cria um vetor para a entrada e um vetor para a saída
dados_estimacao = loadmat('identificacao.mat')
matriz_entrada_estimacao = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, 1, 1, -1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, 1, -1, 1, -1, -1, -1, -1, 1, -1, -1])

matriz_saida_estimacao = np.array([0, 0, 0, -0.7920, -1.99140480, -3.3717082291199993, -4.643247459299328, -5.568990441409431, -5.994765427556233, -5.815537134591262, -3.9865335039306564, -2.0422185065353915, 0.6713570678852745, 2.4724553540899774, 2.9910808879633084, 2.2420875651926386, 0.46203720099713874, -1.9250004537976615, -4.410035883138732, -6.503060531763731, -7.827069021287276, -8.182721020420592, -7.513716403851425, -4.841952123891564, -0.7670558403766707, 3.73909275551855, 6.587213439446999, 7.278342729585356, 5.915583958820836, 4.039662152439177, 0.9388752900100656, -2.777522033705934, -6.323156533011645, -9.02625967983636, -10.364333265326785, -9.055256410690655, -6.607426476493727, -2.4815958232104687, 2.4229715854256435, 5.951200124527024, 8.640728478290459, 10.116194101873361, 10.164139222824886, 8.826450270896444, 5.341162413783521, 1.6019849957132055, -2.746088001700417, -6.840961091171507, -8.702352421876522, -8.13099173055069, -6.619866415026451, -4.539731167699543, -1.1378720861404858, 2.892355776689506, 6.706642192387448, 9.523582262734408, 9.745364632218555, 8.579367366692727, 5.316079721073049, 1.7837985310482973, -2.347522472341825, -5.134463447524262, -6.107845277868994, -6.419180820129581, -6.123335134504718, -5.309208712556798, -4.176921185211803, -2.9096120988500385, -0.6386620154095193, 1.064226902533016, 2.951234946650489, 3.5451192737547252, 2.7389332860417936, 0.8136509069222431, -1.716887588602512, -3.12983741073939, -3.165237649923638, -1.9347699009707466, 0.17073179416573425, 1.4908880665438087, 1.7587499423004398, 1.016421584347618, -0.519276484203351, -2.4297840204794414, -3.131035605281225, -2.507945942121237, -0.8561283263846706, 0.2445614193112529, 0.6113372583366083, 1.4283792918291178, 2.569623021243628, 3.7747040136229164, 4.807901464367981, 5.4808093434893665, 5.629966320774703, 4.14070707878237, 2.4806654751915973, -0.11514678610235851, -3.160374119270379, -6.0108038408334235, -8.071629989267395, -7.876053037129583, -6.687094479171727, -3.7700550791606355, -0.9182465842229963, 1.2906185952728857, 3.6201103857865675, 4.549329886522527, 5.104148682681053, 5.23283965237557, 3.7384021275688695, 1.027404932856097, -1.0830301115972603, -2.161510382547232, -2.150555930455296, -2.3160682621315423, -2.623055604353875, -1.801017036012822, -0.027992131154265687, 2.2658598174794142, 4.599033982206929, 6.45479307338086, 6.383738556228958, 5.599717806908245, 3.2083675830460088, -0.23320046796459562, -2.8336295412923644, -5.210521916281052, -5.817977870987529, -4.643106412460694, -3.2520373520085317, -1.9967954009833564, -1.0367539067411584, 0.5857829018143319, 1.3913054077559774, 1.1998116251149127, 0.14178538720071615, -1.5161575719627018, -3.4060983861960117, -5.14375611437272, -6.403074973773983, -6.9154449464705, -5.512465523500426, -3.665818806507592, -0.6672634940416633, 2.8423891041864704, 4.939073100500848, 5.316165561441745, 5.1688696562743175, 3.4468408292318315, 0.5786830067556974, -1.6492469463990818, -3.9116106049928234, -4.665404332864937, -3.7897061333017956, -1.5960372215982406, 1.3346542951805807, 3.2519197854938215, 4.9150541125450635, 4.97992005510923, 4.650978179991342, 4.110486550926734, 3.4001082357983674, 1.4896943813545196, -1.2302037336926435, -4.095267907837611, -5.356462420129012, -4.8189314322494585, -2.737467970908024, 0.3109746354792424, 2.535976139201614, 4.682753225093657, 6.365058094741578, 6.147724825099754, 5.274962843147623, 2.8644548220145203, -0.528009123998243, -3.0257784110136585, -5.2704079663685555, -5.743910406364771, -4.399535610913549, -1.653978066149325, 1.8583820052654163, 5.396921154178474, 8.212667877018609, 8.62804304441323, 6.733029222537255, 4.209365378952774, 0.4758484310744222, -3.735657558139743, -7.493155027986958, -8.919950609086591, -7.843510532363166, -4.73625653925031, -1.5359598821041924, 1.1184273115252654, 3.9526971395104926, 6.4693504467697185, 8.129143809268532, 7.492211600862761, 4.844428577609366, 2.051362168642882, -0.26720182681148885, -1.7710161720999629, -3.3511779989143546, -3.640462091835361, -3.719753951253235, -2.552521356230478, -1.5553493979483322, -0.9980520792618062, -0.876570419077632, -0.0008808882199491386, 1.4129160714762143, 1.8495191995130096, 1.2311364644316882, -0.16849542381175725, -0.8369370470392148, -0.688911176571771, -1.0147704629381469, -1.7820664858452695, -2.734246633955978, -2.4905832027688986, -1.1778497084480044, -0.33157116023790667, -0.0874906750390349, 0.6916371442374778, 0.6959018889573103, -0.0414434559723976, -0.17825297863198955, -0.7923079217733449, -0.6274363355043004, 0.31370575096708897, 1.7110040199478964, 2.1379053684274747, 2.6988239263698386, 3.299767454248737, 2.6776143051695582, 2.1043623581654574, 0.5865984279296624, -1.5978401161831317, -3.895622637998898, -4.671079840601031, -3.877385462887382, -2.9268914571619447, -0.9573800187400499, 0.5311672285109118, 2.382911380607585, 4.239696322522028, 4.596331658962641, 4.5557255930308775, 3.114511362156725, 1.6949671635348145, -0.5251368021525452, -3.0834183658534284, -4.253381882690204, -3.906564010476637, -3.423504799685907, -2.9149251479378604, -1.3420680992347078, -0.14876918308927428, 1.5626316741558055, 3.508775339397447, 5.215058210811162, 5.187226117749029, 3.550369113967014, 1.943580643596798, 0.7430800689629473, 0.13711113127968783, 0.2017850825196008, 0.8134739262924978, 0.687399821286129, 0.9587425290351441, 0.4447425591121802, -0.7838454692244905, -2.3556793374477634, -2.758803985098325, -1.9321266179892662, -0.14387920859825415, 2.1896990393833584, 4.5737254410942105, 6.541577358628247, 7.682331716163475, 6.651585569078413, 3.742953871167089, -0.2625000150718291, -3.32271753810506, -4.843981705641171, -4.661737615527977, -2.9960956102085268, -1.4077381198618544, 0.916119157367618, 3.493690582755163, 4.66197743445018, 5.359248760392836, 4.384423430779608, 1.9645729892103079, -1.3027639582057293, -4.663484312321874, -6.331993405034233, -7.226903558578272])

#lê os dados de validação do Matlab e cria um vetor para a entrada e um vetor para a saída
dados_validacao = loadmat('validacao.mat')
dados_entrada_validacao = np.array([-1, -1, -1, 1, -1, -1, -1, 1, -1, 1, 1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, -1, 1, -1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, 1, 1, -1, -1, -1, 1, -1, -1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, -1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, -1, 1, -1, -1, 1, 1, -1, 1, 1, -1, -1, -1, -1, -1, 1, -1, 1, -1, 1, -1, 1, 1, -1, -1, -1, -1, -1, -1, 1, 1, 1, -1, 1, -1, 1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, -1, 1, 1, -1, 1, -1, 1, -1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, 1, -1, 1, 1, 1, 1, -1, 1])
dados_saida_validacao = np.array([0.0, 0.0, 0.0, -0.732, -0.7025408, -1.1268885875199999, -1.9653411124602878, -2.947339564421348, -2.7499565023350536, -2.554660740473754, -1.2991842623035028, 0.7211028573394351, 1.9123011700739, 3.224786511169522, 4.418483096804548, 4.127323114736089, 3.638644029621844, 3.08616179212472, 1.3787813923366714, -1.0709429481135846, -2.532225393668728, -2.728897227407916, -1.7922100698098289, -1.1111470375754606, 0.3158492362145974, 2.2405616561744, 4.233429390165847, 5.846282373334615, 5.608571472717746, 3.635971685492547, 0.45697959296459834, -3.2236304089901573, -6.652673192359512, -9.123273297912185, -9.042597140847034, -6.6083001937963965, -3.670101168152449, -0.9029516941763656, 1.18298769628333, 2.230702003695472, 2.115412427658095, 1.0067585179540257, 0.3197486161819352, -0.899176421171183, -1.3331180638822184, -2.0537371816827656, -2.988329497732594, -3.9201148863552655, -4.6725003261082945, -5.051953337884673, -3.887976478066268, -2.5778460053225967, -0.28677947406031845, 2.554658470626929, 5.274244767399551, 6.172077216634757, 5.140062873816096, 2.598916547148088, 0.3372651573509706, -1.2162216713306468, -3.0133276041301937, -4.693184702930305, -4.738976401017439, -3.2579728434413444, -1.7919567271213097, 0.4938958602497808, 3.11820183340353, 4.402657141277039, 5.257722873228008, 4.448552130548651, 2.229453704248128, 0.3413673119876761, -0.8682809783946128, -2.354772296510842, -2.6902651215294813, -1.811943677906454, -0.059793070605233145, 0.9791585872366246, 1.0861485647676763, 0.38569728247273005, 0.19623484736829483, -0.5984165838284747, -1.8234284380053711, -2.005158824933035, -1.1809495097471356, -0.7857038009518589, -0.9306072711081153, -1.472513236612609, -1.1544409218636353, -1.2173980897697638, -1.6454898482466909, -1.1847422535848295, -1.0506873404302852, -0.1437438538744787, 1.3297712080503703, 1.837088351500826, 1.3466633431352129, 1.2279318788975373, 1.542689530372017, 2.1828170636473554, 2.942666929985215, 2.539977817450972, 2.195746582368422, 0.8721934520531899, -1.188123867952897, -3.450673816802038, -4.279958116880779, -3.552002795082471, -1.540473330357928, 1.210831550854518, 2.9862684753256508, 4.569815793204254, 4.628123304543315, 4.361435661597005, 3.9347503158001036, 3.363754742063703, 1.589309525182334, -0.9641830792041695, -2.541983628124928, -2.8445627080590423, -1.923352963598194, -0.04611277539081077, 2.35007749631713, 4.761017647272481, 6.657355010635396, 6.584466612254589, 5.759773039288004, 3.2997219718632973, -0.22312540369311565, -2.9006826369183862, -5.395885332448434, -7.261787806834022, -7.0401404632396565, -6.050071284597635, -4.625569052968101, -3.057764431867501, -1.6658258781363795, -0.6460078030698669, 0.9564423979063843, 1.671293439386973, 1.34159116093435, 0.12820300681123542, -1.6107881475729127, -2.372284378421555, -3.1373281099902046, -2.6568322814956753, -1.029637074052133, 1.3230350912450095, 3.8338889714536823, 4.817505751940381, 4.188084424807113, 3.329138591618782, 1.3661870484606111, -0.13568692731797427, -0.831534589936509, -0.7258041705106948, -1.0201775051387596, -0.5730221195116472, -0.6269141293568985, -1.2218572774672223, -2.122597317470124, -1.9503239347319234, -0.7484970282655303, 1.1568439223521028, 3.28611168671941, 4.083228680373913, 4.548939634380125, 3.5774661335475026, 2.5624228138798575, 1.7929923293323764, 1.3809443555092007, 1.3835959926767556, 1.7083713432998373, 1.0831607376236119, -0.30900983909904367, -1.00002707112712, -2.026932326631699, -3.2491694422686437, -4.396507850102797, -5.195692327956221, -4.3318053507365715, -2.028036257362209, 1.084972383557471, 3.2200800111103796, 5.150710625911257, 6.60226564105114, 7.310473813959033, 7.137631956714549, 5.057629825072442, 2.6731996889308687, -0.569963764110889, -2.880542838109355, -3.791111963299526, -3.309240317735613, -2.754018722564223, -1.1843958418461256, -0.08143829070078867, 0.347601947596047, 1.2741274806685328, 2.4864366825182, 2.5884047316302574, 2.762022592052635, 2.99234403166525, 2.0271552160436217, 0.07793471693104731, -2.3885961329662897, -4.857631882115109, -6.788823634850092, -6.722663171731143, -5.877348437498161, -3.4353934044220287, -1.027959087624004, 1.9162560536766096, 3.7490511222180394, 5.294064253857458, 6.301852147413161, 5.412802889424967, 2.8765360526079924, -0.6764335023304757, -4.482772224380227, -7.783573180739856, -9.91594213770259, -9.368512935145391, -6.379243611817162, -1.7872348761043397, 2.273525623323195, 6.108927449107129, 7.951003495946953, 8.688719116119042, 8.290588214760861, 5.775057347909313, 2.909205153402726, 0.35983606560204806, -1.419884089297662, -2.1382392332334126, -1.7963285283617967, -1.7250685836732553, -1.9877375287520902, -2.4331412456993116, -1.7792871024214851, -0.22531731227463792, 0.6590831900244204, 0.746032715595695, 1.277964202525602, 2.1847667370928976, 3.1877571136237486, 2.963013966923334, 2.7610559373288814, 2.644356198578121, 1.4257728346487584, -0.6410033296108101, -3.0166372048358414, -4.034613516649438, -3.5888575987091325, -3.0161803042507613, -1.3187557555782177, 1.1133566790146427, 2.549410334571294, 2.779563974324949, 3.04899501669982, 3.3690880621126316, 3.659457510203458, 3.809063563112938, 2.613730942437683, 0.39707223933695157, -1.1336067702768964, -1.666108256373794, -1.2464049036054048, -1.1494750260052347, -0.2552727881824328, 1.287596819616087, 3.0523848260008966, 3.558635329251626, 3.917034893499352, 4.0940960652292935, 2.9256526029721734, 1.8589920297259401, 1.1175739935746263, -0.32223747629212307, -1.0691310809041683, -2.071182953189755, -2.077488395906305, -2.2579288765533954, -2.5933057892284994, -1.8625889685960788, -1.4072447911820107, -1.3789288678113363, -1.7329031016694567, -2.315621264314901, -1.8108546213370156, -0.3887965500871008, 0.4053873119192356, 0.45816084991585126, 0.9543918471872541, 0.7059901870328628, 0.9180312181980952, 1.6026699104214503, 2.5724172861957997, 3.56163244189725, 3.2508292301454973])

#cria matriz referentes aos coeficientes do denominador
fi_polos = np.ones((num_amostras, num_polos))

#cria matriz referentes aos coeficientes do numerador
fi_zeros = np.zeros((num_amostras, num_zeros+1))

#inicializa vetores que irão armazenar os coeficientes
num = []
den = []

#----------------------- CRIAÇÃO DA MATRIZ DE REGRESSORES -----------------------

#atribui os valores referentes aos polos
for i in range(0, num_amostras):
    for j in range(0, num_polos):
        fi_polos[i, j] = -matriz_saida_estimacao[i-1]

#ajuste dos valores para a posição correta nas colunas
for j in range(1, num_polos):
    coluna = fi_polos[:, j].copy()
    coluna = np.roll(coluna, j)
    fi_polos[:, j] = coluna

#atribui zero para as amostras negativas 
for i in range(0, num_amostras):
   for j in range(0, num_polos):
        if i - vetor_sub_polos[j] < 0:
                fi_polos[i, j] = 0            

#atribui os valores referentes aos zeros
for i in range(0, num_amostras):
     for j in range(0, num_zeros+1):
          fi_zeros[i, j] = matriz_entrada_estimacao[i]

#ajuste dos valores para a posição correta nas colunas
for j in range(1, num_zeros+1):
     coluna = fi_zeros[:, j].copy()
     coluna = np.roll(coluna, j)
     fi_zeros[:, j] = coluna

#atribui zero para as amostras negativas
for i in range(0, num_amostras):
     for j in range(0, num_zeros+1):
          if i - vetor_sub_zeros[j] < 0:
               fi_zeros[i, j] = 0

#junta as matrizes dos polos e dos zeros formando a matriz de regressores
fi = np.hstack((fi_polos, fi_zeros))  

#-------------------------------------------------------------------------------

#identifica os coeficientes da função de tranferência pelo método dos mínimos quadrados
coefficients, _, _, _ = np.linalg.lstsq(fi, matriz_saida_estimacao)

#coeficiente de maior grau do denominador unitário
den.append(1)

#gera vetor com os coeficientes do denominador e numerador
for i in range(0, len(coefficients)):
     if i < num_polos:
          den.append(coefficients[i])
     else:
          num.append(coefficients[i])

#gera função de transferência para um período de amostragem de 1 segundo
tfunc = TransferFunction(num, den, dt=1)

#imprime a função de transferência
print(f'\033[1;37m{tfunc}\033[m')

#cria uma figura 2X2 com quatro gráficos
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

#obtém a resposta do sistema para o primeiro conjunto de dados
saida_estimacao = lsim(tfunc, matriz_entrada_estimacao, T=None)

#obtém a resposta do sistema para o segundo conjunto de dados
saida_validacao = lsim(tfunc, dados_entrada_validacao, T=None)

#------------------- CONFIGURAÇÕES DE LAYOUT -------------------

ax1.set_title('Sistema original')
ax1.set_xlabel('Amostras')
ax1.set_ylabel('Amplitude')

ax2.set_title('Sistema estimado')
ax2.set_xlabel('Amostras')
ax2.set_ylabel('Amplitude')

ax3.set_title('Sistema original - Validação')
ax3.set_xlabel('Amostras')
ax3.set_ylabel('Amplitude')

ax4.set_title('Sistema estimado - Validação')
ax4.set_xlabel('Amostras')
ax4.set_ylabel('Amplitude')

plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

#---------------------------------------------------------------

#plota a saída do sistema para o primeiro conjunto de dados
ax1.plot(matriz_saida_estimacao)

#plota a saída do sistema referente a função de transferência obtida com o primeiro conjunto de dados
ax2.plot(saida_estimacao[0])

#plota a saída do sistema para o segundo conjunto de dados
ax3.plot(dados_saida_validacao)

#plota a saída do sistema para a validação
ax4.plot(saida_validacao[0])

#exibe a figura
plt.show()




