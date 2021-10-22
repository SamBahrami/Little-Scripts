import numpy as np
import matplotlib.pyplot as plt
import yaml


def create_histogram_right_wrong(
    wrong: np.array,
    right: np.array,
    num_bins: int = 10,
    save_name: str = "saved.png",
):
    """Create two lines on a plot to show the distribution
    of values

    Parameters
    ----------
    wrong : np.array
        All of the values that the model incorrectly classified
    right : np.array
        Same as wrong, but right
    num_bins : int, optional
        number of bins to have in the histogram, by default 10
    save_name : str, optional
        file name to save it as, by default "saved.png"
    """
    righthist, rightbins = np.histogram(right, bins=num_bins)
    wronghist, wrongbins = np.histogram(wrong, bins=rightbins)
    # scaling so they are roughly in the same scale
    # this makes the y axis represent an abstract form of 'frequency'
    wronghist = wronghist / len(wrong)
    righthist = righthist / len(right)

    plt.plot(wrongbins[:-1], wronghist, label="wrong")
    plt.plot(wrongbins[:-1], righthist, label="right")
    plt.legend()
    plt.savefig(save_name)
    plt.close()


def create_histrogram_from_mask(predictions, mask, num_bins=10, save_name="save.png"):
    """Create a histogram of the values

    Parameters
    ----------
    predictions : list of lists of predictions
        if you have 10 classes, then its a list of lists of size 10
        which represent the 10 different class values that it can take
    mask : List[bool]
        List of true and false values to signify if they were correct or not
        when compared to the ground truth
        e.g. mask = las_data.classification == gd_truth.classification

    Returns
    -------
    None
        saves a figure
    """
    return create_histogram_right_wrong(
        predictions[~mask], predictions[mask], num_bins=num_bins, save_name=save_name
    )
