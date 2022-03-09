# `MetaCall Jupyter Kernel`: IPython और Jupyter का लाभ उठाने वाली MetaCall Core लाइब्रेरी के लिए रैपर कर्नेल

![पायथन सीआई बिल्ड](https://github.com/metacall/jupyter-kernel/actions/workflows/ci.yml/badge.svg)
[![कोड शैली: काला](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![बाइंडर](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/metacall/jupyter-kernel/master)
![संस्करण 0.1.0](https://img.shields.io/badge/Version-0.1.0-brightgreen.svg)
![लाइसेंस: अपाचे 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

## परिचय

MetaCall Jupyter कर्नेल एक ओपन-सोर्स रैपर कर्नेल है जो [MetaCall Core](https://github.com/metacall/core) और [Polyglot REPL](https://github.com/metacall/polyglot-repl) के माध्यम से क्रॉस-लैंग्वेज फंक्शन कॉल्स को लागू करता है। /मेटाकॉल/पॉलीग्लॉट-प्रतिलिपि)। मेटाकॉल कोर एक ओपन-सोर्स लाइब्रेरी है जो डेवलपर्स के लिए पॉलीग्लॉट प्रोग्रामिंग अनुभव लाता है। मेटाकॉल के साथ, डेवलपर्स उपयोग में आसान उच्च-स्तरीय एपीआई के माध्यम से विभिन्न प्रोग्रामिंग भाषाओं को एम्बेड कर सकते हैं।

कर्नेल मेटाकॉल कोर एपीआई को उजागर करता है जिसे ज्यूपिटर नोटबुक इंटरफ़ेस के माध्यम से लोड और लॉन्च किया जा सकता है। इस नोटबुक के साथ,
उपयोगकर्ता विभिन्न प्रोग्रामिंग भाषाओं में कोड लिखने, मिश्रण करने और एम्बेड करने का प्रयास कर सकते हैं। यह परियोजना [PyPi](https://pypi.org/project/metacall-jupyter/) पर उपलब्ध है।

## प्रमुख विशेषताऐं

`metacall_jupyter` को निम्नलिखित प्रमुख विशेषताओं के साथ सरल और संक्षिप्त होने के लिए डिज़ाइन किया गया है:

- आप क्रॉस-लैंग्वेज फंक्शन कॉल के जरिए विभिन्न प्रोग्रामिंग भाषाओं में फंक्शन कॉल कर सकते हैं।
- आप विभिन्न प्रोग्रामिंग भाषाओं में कोड निष्पादित करने के लिए एक उच्च स्तरीय एपीआई का उपयोग करते हैं।
- मेटाकॉल के मेटा-ऑब्जेक्ट प्रोटोकॉल से सभी उपलब्ध कार्यों और मॉड्यूल को सूचीबद्ध करता है।
- पॉलीग्लॉट आरईपीएल के साथ पायथन और नोडजेएस के लिए आधिकारिक समर्थन।
- पॉलीग्लॉट विकास और घटकों के आसपास केंद्रित सरल और सहज उपयोगकर्ता-अनुभव।

## स्थापना

आपकी निर्भरता और एप्लिकेशन बिल्ड को प्रबंधित करने के लिए वर्चुअल वातावरण का उपयोग करने की अनुशंसा की जाती है। हम सबसे पहले स्थानीय परियोजना पर्यावरण की स्थापना के साथ शुरुआत करेंगे:

```sh
git clone https://github.com/metacall/jupyter-kernel.git
virtualenv env
source env/bin/activate
```

आगे हम सभी आश्रितों को डाउनलोड कर सकते हैं और कर्नेल को सेटअप कर सकते हैं:

```sh
curl -sL https://raw.githubusercontent.com/metacall/install/master/install.sh | sh
python3 -m pip install --upgrade pip
pip3 install -r requirements.txt
python3 setup.py install
python3 -m metacall_jupyter.install
metacall npm install
```

निम्नलिखित कमांड को पुश करके अपना ज्यूपिटर नोटबुक शुरू करें:

```sh
python3 -m metacall_jupyter.launcher
```

आप ड्रॉप-डाउन विकल्पों में से `metacall_jupyter` चुन सकते हैं और जुपिटर नोटबुक इंटरफ़ेस के साथ काम करना शुरू कर सकते हैं। उदाहरण नोटबुक [यहाँ] (उदाहरण) पाए जाते हैं।

## डोकर

छवि बनाएं:

```sh
docker build -t metacall/jupyter .
```

छवि चलाएँ:

```sh
docker run --rm --network=host -it metacall/jupyter
```

## परिक्षण

परीक्षण चलाने के लिए, निम्नलिखित कमांड को पुश करें:

```sh
pytest test-kernel.py
```

स्क्रिप्ट सभी परीक्षण चलाएगी। एक कवरेज रिपोर्ट तैयार करने के लिए, हम `pytest-cov` प्लगइन का उपयोग कर रहे हैं, जिसे निम्नलिखित कमांड को पुश करके लागू किया जा सकता है:

```sh
pytest --cov=metacall_jupyter test-kernel.py
```

## दस्तावेज़ीकरण

हमारा आधिकारिक दस्तावेज [**metacall-jupyter-kernel.readthedocs.io**](https://metacall-jupyter-kernel.readthedocs.io/en/latest/index.html) पर उपलब्ध है।

दस्तावेज़ को संपादित करने के लिए आपको एक GitHub खाते की आवश्यकता है। एक बार जब आप एक बना लेते हैं और लॉग इन कर लेते हैं, तो आप संबंधित फाइल पर नेविगेट करके और एडिट (पेन) आइकन पर क्लिक करके किसी भी पेज को एडिट कर सकते हैं। वैकल्पिक रूप से एक कांटा बनाएं, और फिर रेपो और `cd` को `docs` निर्देशिका में क्लोन करें। आइए हम दस्तावेज़ीकरण सेट करें:

```sh
virtualenv env
source env/bin/activate
pip install -r requirements.txt
make html
```

अब आप अपने ब्राउज़र में `_build/html/index.html` पर दस्तावेज़ीकरण साइट खोल सकते हैं। दस्तावेज़ीकरण साइट पर संबंधित परिवर्तन करें और फिर दस्तावेज़ को अद्यतन करने के लिए `make clean && make html` चलाएं। अब आप अपने परिवर्तनों को अपस्ट्रीम शाखा में मिलाने के लिए एक पुल अनुरोध बना सकते हैं।

## योगदान

योगदान के साथ आरंभ करने के लिए, [आचार संहिता](../CODE_OF_CONDUCT.md) देखें और आरंभ करने के लिए एक [समस्या](https://github.com/metacall/jupyter-kernel/issues/new) बनाएं।

यदि आप Git और GitHub में नए हैं, तो आप अधिक जानकारी [यहां] (https://metacall-jupyter-kernel.readthedocs.io/en/latest/contributing.html) पा सकते हैं। इसमें परिवर्तन करने, लाइनिंग करने, सीआई को स्थानीय रूप से चलाने और पुल अनुरोध सबमिट करने के बारे में सभी जानकारी शामिल है।

आप यह देखने के लिए [चेंज लॉग](../CHANGELOG.md) देख सकते हैं कि परियोजना की स्थापना के बाद से इसमें क्या बदलाव आया है।

## लाइसेंस

[अपाचे-2.0 लाइसेंस](../LICENSE)