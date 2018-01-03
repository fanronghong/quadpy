# -*- coding: utf-8 -*-
#
from mpmath import mp

from .helpers import _s3, _s21, _s111
from ..helpers import untangle


class ZhangCuiLiu(object):
    '''
    Linbo Zhang, Tao Cui and Hui Liu,
    A set of symmetric quadrature rules on triangles and tetrahedra,
    Journal of Computational Mathematics
    Vol. 27, No. 1 (January 2009), pp. 89-96,
    <http://www.jstor.org/stable/43693493>.

    Abstract:
    We present a program for computing symmetric quadrature rules on triangles
    and tetrahedra. A set of rules are obtained by using this program.
    Quadrature rules up to order 21 on triangles and up to order 14 on
    tetrahedra have been obtained which are useful for use in finite element
    computations. All rules presented here have positive weights with points
    lying within the integration domain.
    '''
    # pylint: disable=line-too-long
    def __init__(self, index, mpmath=False):
        self.name = 'ZCL({})'.format(index)

        flt = mp.mpf if mpmath else float

        mp.dps = 35
        if index == 1:
            self.degree = 8
            data = [
                (flt('0.1443156076777871682510911104890646'), _s3(mpmath)),
                (flt('0.1032173705347182502817915502921290'), _s21(flt('0.1705693077517602066222935014914645'))),
                (flt('0.0324584976231980803109259283417806'), _s21(flt('0.0505472283170309754584235505965989'))),
                (flt('0.0950916342672846247938961043885843'), _s21(flt('0.4592925882927231560288155144941693'))),
                (flt('0.0272303141744349942648446900739089'), _s111(flt('0.2631128296346381134217857862846436'), flt('0.0083947774099576053372138345392944'))),
                ]
        elif index == 2:
            self.degree = 14
            data = [
                (flt('0.0585962852260285941278938063477560'), _s3(mpmath)),
                (flt('0.0017351512297252675680618638808094'), _s21(flt('0.0099797608064584324152935295820524'))),
                (flt('0.0261637825586145217778288591819783'), _s21(flt('0.4799778935211883898105528650883899'))),
                (flt('0.0039197292424018290965208275701454'), _s21(flt('0.1538119591769669000000000000000000'))),
                (flt('0.0122473597569408660972869899262505'), _s21(flt('0.0740234771169878100000000000000000'))),
                (flt('0.0281996285032579601073663071515657'), _s21(flt('0.1303546825033300000000000000000000'))),
                (flt('0.0508870871859594852960348275454540'), _s21(flt('0.2306172260266531342996053700983831'))),
                (flt('0.0504534399016035991910208971341189'), _s21(flt('0.4223320834191478241144087137913939'))),
                (flt('0.0170636442122334512900253993849472'), _s111(flt('0.7862373859346610033296221140330900'), flt('0.1906163600319009042461432828653034'))),
                (flt('0.0096834664255066004075209630934194'), _s111(flt('0.6305521436606074416224090755688129'), flt('0.3623231377435471446183267343597729'))),
                (flt('0.0363857559284850056220113277642717'), _s111(flt('0.6265773298563063142335123137534265'), flt('0.2907712058836674150248168174816732'))),
                (flt('0.0069646633735184124253997225042413'), _s111(flt('0.9142099849296254122399670993850469'), flt('0.0711657108777507625475924502924336'))),
                ]
        else:
            assert index == 3
            self.degree = 20
            data = [
                (flt('0.0125376079944966565735856367723948'), _s3(mpmath)),
                (flt('0.0274718698764242137484535496073598'), _s21(flt('0.2158743059329919731902545438401828'))),
                (flt('0.0097652722770514230413646914294237'), _s21(flt('0.0753767665297472780972854309459163'))),
                (flt('0.0013984195353918235239233631597867'), _s21(flt('0.0103008281372217921136862160096969'))),
                (flt('0.0092921026251851826304282034030330'), _s21(flt('0.4936022112987001655119208321450536'))),
                (flt('0.0165778760323669253260236250351840'), _s21(flt('0.4615509381069252967410487102915180'))),
                (flt('0.0206677623486650769614219700129729'), _s111(flt('.3286214064242369933034974609509133'), flt('.4293405702582103752139588004663984'))),
                (flt('0.0208222355211545073068785561993297'), _s111(flt('.2604803617865687564195930170811535'), flt('.1015775342809694461687550061961797'))),
                (flt('0.0095686384198490606888758450458320'), _s111(flt('.1370742358464553000000000000000000'), flt('.7100659730011301599879040745464079'))),
                (flt('0.0244527709689724638856439207024089'), _s111(flt('.1467269458722997843041609884874530'), flt('.4985454776784148493896226967076119'))),
                (flt('0.0031557306306305340038264003207296'), _s111(flt('.0269989777425532900000000000000000'), flt('.0491867226725820016197037125775872'))),
                (flt('0.0121367963653212969370133090807574'), _s111(flt('.0618717859336170268417124700122339'), flt('.7796601465405693953603506190768108'))),
                (flt('0.0149664801438864490365249118515707'), _s111(flt('.0477243674276219962083526801042934'), flt('.3704915391495476369201496202567388'))),
                (flt('0.0063275933217777395693240327504398'), _s111(flt('.1206005151863643799672337870400794'), flt('.8633469487547526484979879960925217'))),
                (flt('0.0013425603120636958849798512981433'), _s111(flt('.0026971477967097876716489145012827'), flt('.0561949381877455029878923019865887'))),
                (flt('0.0027760769163475540677293561558015'), _s111(flt('.0030156332779423626572762598234710'), flt('.2086750067484213509575944630613577'))),
                (flt('0.0107398444741849415551734474479517'), _s111(flt('.0299053757884570188069287738643386'), flt('.7211512409120340910281041502050941'))),
                (flt('0.0053678057381874532052474100212697'), _s111(flt('.0067566542224609885399458175192278'), flt('.6400554419405418899040536682721647'))),
                ]

        self.bary, self.weights = untangle(data)
        self.points = self.bary[:, 1:]
        return
