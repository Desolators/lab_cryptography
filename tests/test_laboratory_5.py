from unittest import TestCase, main
from laboratories.libraries import maths_thinks


class Laboratory5Test(TestCase):
    def test_encryption_task_1(self):
        self.assertEqual(maths_thinks.encryption(52, 57230432725785700753577, x=189462941526557263979509, key='task_1'),
                         (188193154944763700666162, 57230432725785700753577))
        self.assertEqual(maths_thinks.encryption(502, 37827977577900409532279, x=161076090094398216774913, key='task_1'),
                         (126789136886854837729260, 37827977577900409532279))
        self.assertEqual(maths_thinks.encryption(12, 1071651753144086580713, x=160794391105011804385489, key='task_1'),
                         (73814355306185611871856, 1071651753144086580713))
        self.assertEqual(maths_thinks.encryption(5222, 48145352275897071181193, x=404393756428668921354191, key='task_1'),
                         (312582718651960383902872, 48145352275897071181193))
        self.assertEqual(maths_thinks.encryption(982, 143828727644991409392389, x=404393756428668921354191, key='task_1'),
                         (389881053557770822591571, 143828727644991409392389))
        self.assertEqual(maths_thinks.encryption(3, 66665618066761223805005, x=165349908009529903192921, key='task_1'),
                         (49466997347214955262675, 66665618066761223805005))


if __name__ == '__main__':
    main()
