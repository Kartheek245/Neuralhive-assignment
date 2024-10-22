create_folders_with_json() {
  min=$1
  max=$2
  
  for ((i=min; i<=max; i++)); do
    folder="step-$i"
    mkdir -p "$folder"
    echo "{\"name\": \"step-$i\"}" > "$folder/data.json"
  done
}

create_folders_with_json 1 5