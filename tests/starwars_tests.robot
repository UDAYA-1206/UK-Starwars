*** Settings ***
Library           ../lib/APIKeywords.py
Library           ../lib/UIKeywords.py
Variables         test_data.yaml

*** Test Cases ***

Verify Movie Count
     [Tags]    Testcase 1    API
    Verify Movies Count    ${api_base}    ${expected_movie_count}

Verify Director Of Third Movie
     [Tags]    Testcase 2    API
    Verify Movie Director    ${api_base}    ${third_movie_index}    ${third_movie_director}

Verify Producers Not Present
    [Tags]    Testcase 3    API
    Verify Producer Not Match    ${api_base}    ${fifth_movie_index}    ${invalid_producers}

Verify Species Present In Movie
    [Tags]    Testcase 4    UI
    Verify Species In Movie    ${api_base}    ${species_movie_title}    ${expected_species}

Verify Planet Not Present In Movie
    [Tags]    Testcase 5    UI
    Verify Planet Not In Movie    ${api_base}    ${planet_movie_title}    ${unexpected_planet}

Verify Sorted Last Movie Title
    [Tags]    Testcase 6    UI
    Verify Sorted Last Movie Title    ${api_base}    ${planet_movie_title}