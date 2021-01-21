## happy path

* pembukaan
    - utter_greet
* kondisi_baik
    - utter_happy

## diagnosis path 1

* pembukaan
    - utter_greet
* kondisi_tidak_baik
    - utter_help
* tanya_umur
    - utter_umur
* tanya_berat
    - utter_berat
* gejala
    - action_handle_symptom
* gejala
    - action_handle_symptom
* penolakan
    - utter_alternative
* gejala
    - action_handle_symptom
* gejala
    - action_handle_symptom
* penolakan
    - utter_alternative
* gejala
    - action_handle_symptom
* penolakan
    - utter_alternative
* penolakan
    - action_diagnosis

## diagnosis path 2

* pembukaan
    - utter_greet
* kondisi_tidak_baik
    - utter_help
* tanya_umur
    - utter_umur
* tanya_berat
    - utter_berat  
* gejala
    - action_handle_symptom
* penolakan
    - utter_alternative
* gejala
    - action_handle_symptom
* gejala
    - action_handle_symptom
* gejala
    - action_handle_symptom
* penolakan
    - utter_alternative
* gejala
    - action_handle_symptom
* penolakan
    - utter_alternative
* pengakhiran
    - action_diagnosis
    - utter_did_that_help

## diagnosis path 3

* pembukaan
    - utter_greet
* kondisi_tidak_baik
    - utter_help
* tanya_umur
    - utter_umur
* tanya_berat
    - utter_berat  
* gejala
    - action_handle_symptom
* gejala
    - action_handle_symptom
* gejala
    - action_handle_symptom
* gejala
    - action_handle_symptom
* gejala
    - action_handle_symptom
* gejala
    - action_handle_symptom
* pengakhiran
    - action_diagnosis
    - utter_did_that_help