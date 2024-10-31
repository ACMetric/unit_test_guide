"""
Module containing various auxiliary functions for data preprocessing, calculations, and analysis.

This module provides a collection of utility functions that are used for a variety of tasks,
including data manipulation, calculation of statistics, and printing of results.

Functions:
    - get_always_valid_bounds
    - get_xp_length_in_days
    - get_xvar_names
    - get_flight_week
    - get_route_data
    - interpolate
    - increase_date_by_x_days
    - get_date_mask
    - get_exclude_mask
    - get_dow
    - add_columns
    - get_treatment_cycles
    - set_modulo_treatment_effect
    - collect_results_df
    - include_both_directions
    - is_in_period
    - get_bin_number
    - get_hourly_cdf_departure
    - select_groups
    - final_te_print
"""

from datetime import datetime, timedelta
from typing import List, Optional, Tuple, Type

import numpy as np
import pandas as pd
import scipy.stats as st
from scipy.optimize import minimize


def eq_zeros(x: float, prob: float) -> float:
    """
    The function for minimization to compute the cirtical value for probability lines for scale/stop decision

    Parameters
    ----------
    x: float
        The function input for critical value
    prob: float
        The probability level for scale-up/stop decision lines

    Returns
    -------
    float
        The value to be minimized
    """
    z = st.norm.ppf(1 - prob / 2) ** 2
    y = (
        np.log(st.norm.cdf(np.sqrt(z / (1 + z)) * x))
        + z / (2 * (1 + z)) * x**2
        + np.log(2 * np.sqrt(1 / (1 + z)))
        + np.log(prob)
    )
    return y**2


def get_critical_value(prob: float) -> float:
    """
    Returns the cirtical value for probability lines for scale/stop decision

    Parameters
    ----------
    prob: float
        The probability level for scale-up/stop decision lines

    Returns
    -------
    float
        The cirtical value for probability lines for scale/stop decision
    """
    opt_result = minimize(lambda x: eq_zeros(x, prob), x0=1, method="BFGS")
    assert opt_result.fun <1e-7
    return opt_result.x[0]
