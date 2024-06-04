while IFS= read -r line; do
    echo $line
    python3 get-summary.py $line
done < links
