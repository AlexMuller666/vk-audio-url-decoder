vk.com audio url decoder
=======================

Usage:

.. code:: python

    import vaud

    uid = 1
    url = 'https://m.vk.com/mp3/audio_api_unavailable.mp3?extra=zuHdAgfLvxaXtd1W...CsDasdvv32yLjpy3yVBxrm#AqVYStC'
    decoded_url = vaul.decode(uid, url)

.. code:: python

    import vaud

    uid = 1
    urls = [
        'https://m.vk.com/mp3/audio_api_unavailable.mp3?extra=zuHdAgfLvxaXtd1W...CsDasdvv32yLjpy3yVBxrm#AqVYStC',
        'https://m.vk.com/mp3/audio_api_unavailable.mp3?extra=zuHdAgfLvxaXtd1W...CsDasdvv32yLjpy3yVBxrm#AqVYStC',
        'https://m.vk.com/mp3/audio_api_unavailable.mp3?extra=zuHdAgfLvxaXtd1W...CsDasdvv32yLjpy3yVBxrm#AqVYStC',
    ]
    decoder = vaul.Decoder(uid)
    decoded_urls = []
    for i in urls:
        decoded_urls.append(decoder(url))
