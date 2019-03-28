#! /bin/bash

read -p "Open plot in viewer? (Y/n) " input

if [[ $input == 'n' || $input == 'no' ]]; then

    echo "Printing plot to file ..."
    python src/plot_example.py blah
    echo "... done."

else

    echo "Opening plot ..."
    python src/plot_example.py
    echo "... done."

fi
