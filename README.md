# SF-12 Library

## Overview

This is a python library to calculate  12-item Short Form Survey (SF-12) score. The SF-12 is a general health questionnaire that was first published in 1995 as part of the Medical Outcomes Study (MOS). The SF-12 was constructed using questions drawn from each of the 8 dimensions of the MOS 36-item Short Form Survey (SF-36). It is designed to have similar performance to the SF-36, while taking less time to complete.

Two summary scores are reported from the SF-12:
- **Mental Component Score (MCS-12)**
- **Physical Component Score (PCS-12)**

The scores may be reported as Z-scores (difference compared to the population average, measured in standard deviations). The United States population average PCS-12 and MCS-12 are both 50 points. The United States population standard deviation is 10 points. So each increment of 10 points above or below 50 corresponds to one standard deviation away from the average. For more information, refer to the original publication:

- Ware, John E., Susan D. Keller, and Mark Kosinski. *SF-12: How to score the SF-12 physical and mental health summary scales*. Health Institute, New England Medical Center, 1995.

## Basic Usage

To run the SF-12 script, use the following command:

```bash
poetry run python sf12.py
```

## Development

### Running the Application

To run the application, use:

```bash
poetry run python sf12.py
```

### Running Tests

To run the tests, use:

```bash
poetry run pytest
```


### Publish to pypi


```bash
poetry build 
poetry publish
```