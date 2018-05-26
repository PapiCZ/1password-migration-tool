#!/usr/bin/env python3

import subprocess
import json


def main():
    data_types = ('documents', 'groups', 'items', 'templates', 'users', 'vaults')

    basic_data = {}
    for data_type in data_types:
        p = subprocess.Popen(['op', 'list', data_type], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()

        if err:
            print(str(err, 'utf-8'))
            exit(1)

        basic_data[data_type] = json.loads(str(out, 'utf-8'))

    data_to_export = {}
    for data_type, data in basic_data.items():
        if data_type == 'templates' :
            continue

        data_for_current_type = []
        for value in data:
            p = subprocess.Popen(['op', 'get', data_type[:-1], value['uuid']], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate()

            if err:
                print(str(err, 'utf-8'))
                exit(1)

            data_for_current_type.append(json.loads(str(out, 'utf-8')))
        data_to_export[data_type] = data_for_current_type

    data_to_export['templates'] = basic_data['templates']

    print(json.dumps(data_to_export, ensure_ascii=False))


if __name__ == '__main__':
    main()
