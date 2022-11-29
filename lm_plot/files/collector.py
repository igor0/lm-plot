import glob
import json
import os
import re

def _collect(pathname, meta_extractor) :
    rgx_file_name = re.compile("^(.*)_?eval_results_([0-9-]+).json$")

    dict_list = []
    for file_path in glob.glob(pathname):
        file_name = os.path.basename(file_path)
        m = rgx_file_name.match(file_name)
        if m is None:
            print("WARNING: cannot parse results file name '{}'".format(file_name))
            continue

        header = dict()

        run_id = m[1]
        header['path'] = file_name
        header['timestamp'] = m[2]

        # Parse the file name and add
        metadata_run_id = meta_extractor.from_run_id(run_id)
        if metadata_run_id is None:
            continue

        # Read the json file into a data frame
        with open(file_path) as f:
            try:
                eval_json = json.load(f)
                result_json = eval_json["results"]
            except:
                print("WARNING: cannot load file '{}'".format(file_path), file=stderr)
                continue

        metadata_config = meta_extractor.from_config(eval_json["config"])

        for task in result_json.keys():
            for metric in result_json[task]:
                record = header.copy()
                record["task"] = task
                record["metric"] = metric
                record["value"] = result_json[task][metric]
                record.update(metadata_run_id)
                record.update(metadata_config)

                dict_list.append(record)

    return dict_list
