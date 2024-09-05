import unittest
from score_calculator import sf12_score
import pandas as pd

class ScoreTestCase(unittest.TestCase):
    def test_load(self):
        
        # Test if the file is loaded
        file_path = 'examples/example.csv'
        score_instance = sf12_score.SF12Score(file_path)
        answers = score_instance.load_answers()
        print(answers)
        # Sample data for 3 respondents
                
        data = pd.DataFrame({
            'GH1':  [5, 4],
            'PF02': [2, 1],
            'PF04': [1, 1],
            'RP2':  [1, 1],
            'RP3':  [2, 1],
            'RE2':  [1, 2],
            'RE3':  [2, 2],
            'BP2':  [3, 4],
            'MH3':  [4, 3],
            'VT2':  [3, 5],
            'MH4':  [2, 6],
            'SF2':  [1, 5]
        })

        # Convert keys to lower case
        data.columns = [col.lower() for col in data.columns]

        (pcs, mcs) = score_instance.sf12(data)
        print(pcs)
        print(mcs)
        #  Python floats to IEEE-754 “double precision”.
        self.assertEqual(pcs[1], 18.36726)
        self.assertEqual(mcs[1], 63.09202)
        self.assertAlmostEqual(pcs[0], 34.73346) 
        self.assertAlmostEqual(mcs[0], 34.66566) 




if __name__ == '__main__':
    unittest.main()