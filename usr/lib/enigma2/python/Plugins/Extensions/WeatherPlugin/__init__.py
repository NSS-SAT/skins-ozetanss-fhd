�PNG

   IHDR   d   (   ?��q   PLTE                                                       ���(4*=S������vd���3�9<<���zsQ~vXU`q���mdDƌ��������������]agі��962%ait�������˾������'�ubw����"$��_RJ%"
<DS9@I,38����ܹ����ĭ��� ������Xf���������k07@��YKq���+���)(NSVy����n����hdR'6���|��DJRC<���Rx����*CcSI���qx�$4Kk\���X]d���9@G7h�,&������86������!(3��ABIQ����t73��;̞@�����&9?G$?�����p�����P���")1�v��{�^���$��]��^ciZP��\#*������"#	:0.����ܤ���&'MT_��������s�����ء��������lpv̊	/6>MRY���B<MD���PU\,+(/6�fi�������閘�8S|��Dߜmrx���'{f����䠯����fXrv}x{������q
GLV��*TY`���������=CK��}��������������ejo���"   ���9a�}�   tRNS                  �s=?  IDATHǵ��W[���7<�>��.�����֡�Bk)T�Žť��[ "�$"D�{&��D����+�ke����̷��=�x��p��F�|����b�jz��F�&���g��w����0p����@(q�J�_���_��1^�0ǑwYt�^ǵ{����2�u��=�_��֕s��)��ǿ�U��� �B1A�}��kىtz"�㘏(o���?�x����V-��CQ��N&��YN�)�[�e�8��� �y��lzHo��dr"ӡ�4o�cQ3��Qzv9�O�(�?gd��'�$����?Ӑvv���Iʖ��	Ǯ����cf�>��MO�L�D�{�Vt��6Y�(�2�4���)�����'��ޒ�����DfQT:��M��9 �	��=�إ`�s<Pa���)Z�eoj����ѩ��}�٪��_�FG<�{�汾w��,�g!!����ѓg��:2�ϽOT6���W.z+f�w�*��ÕHAv˹G�csrǦ��B��r���z'ה�,Ƀ���I��������}��,�B(�ǜ��l~Y����y��+*s$��"Z�4��n_I���޶B69|(ʩ�������<��J���̙��ء���:EƜ�7���������^�K���EA��Щ�Ǐ��B�́��5�Y�!d<�v~|~~����ͪ��W�Փ������?�
�Q���aO~�@=��@�⣱�F>���`�]�`��(?':pK�͢m�zi�հ}7D)i8�ܜ�t]�)�~��T|�������i�ޑ3�
�g���w#��W����e��嚚B9�An'v2����pq۩ϼv�$���Ս������AvǄ�H����M�n�R���vw*GZ�L�~��7���[3;���l�$���4��qm�x�Д�%ȡ|>ȋ��po�ڵ�_�ɕ���s�d�j�޺���갦b���T]�"����kh�2��x�⁙�����C�H6�8E��W��"�eD��'E"^�����k:��v��ړ��4�ʨ�֑�{�ԇQ��V��qc��Y�[���|�ȭ}�y�Q[YyV��"}t�v�a��O�M��aJB��`�D����~g�;�L�2�����On��Z����'�nc�2()�^�D�N_�w���d���*u�d��H�Vt��Z�Q͓;�>܂o���H�e%wK�������
�}���+g�
��B�.ﵯi?B��tz��8����v3�f6��qΒR���<S�J�~�.�.\w#�I?�F�@N1���a�_�.G\�a7��U����į�ē\�KU[oT,1���^W^�u��6z��z�B�>��'{���� lI�G֗'"��q�D�v���Q0r��Sx�8��I�7�d���CO��^�}׾��/�.^x	]�C�Jw]��+/U�Г�3��՗�z<�ՙZmz!���(���� �\�_��:%��;	�v��SڞK����Wa*L���l?�\�o���o�e�JU�KE�J�����'���F:%�6��`�{���+ �`��qb�l ,�j�6��u�� q  B1\����VY�xM��PY\ #��x�\��e���,�<�f��\}W����~�n��@�\=���
4``�rƴ>�o����_@X���[��� �`4a �=bI�@�dtAՈ���6���i�O�t��� Z� �rM��"j.H� ���x�Hn����sә`d�>c�X�F�-`�yWk�Dr���
�O�&4
 �� ��^7n3d\L3�ЊUD�;��G�q�͜�n4�E�] ͖=��������$ܵA�����8Yp��h�`z7�����ǜwȴ	��6�v�65'� ��Ɠ�����7H@�|�G�d�>���2�*ᕡ�ж�����G�n�V$2����!��iI@�\c�d��� �#5��J���w�54ZFг<�#���h���쨩Y�hAs1(a��#�����F�o�3�xa�o�K>����a��F��4|��/��a�E    IEND�B`�# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
import os,gettext

def localeInit():
	lang = language.getLanguage()[:2] # getLanguage returns e.g. "fi_FI" for "language_country"
	os.environ["LANGUAGE"] = lang # Enigma doesn't set this (or LC_ALL, LC_MESSAGES, LANG). gettext needs it!
	gettext.bindtextdomain("WeatherPlugin", resolveFilename(SCOPE_PLUGINS, "Extensions/WeatherPlugin/locale"))

def _(txt):
	t = gettext.dgettext("WeatherPlugin", txt)
	if t == txt:
		print("[WeatherPlugin] fallback to default translation for", txt)
		t = gettext.gettext(txt)
	return t

localeInit()
language.addCallback(localeInit)

