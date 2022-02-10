from fybrikLogging import fybrikLogging

def test_fahrToKelv():
    '''
    make sure freezing is calculated correctly
    '''

    
    assert fybrikLogging.fahrToKelv(32) == 273.15, 'incorrect freezing point!'
