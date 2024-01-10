#!/bin/bash

DATE=$(date +%Y.%m.%d_%H.%M.%S)
HERE=$(pwd)
LOG_DIR="${HERE}"/.log
if [ ! -d "${LOG_DIR}" ]; then 
    mkdir "${LOG_DIR}"; 
fi

which=${1:-run}
THIS_START=$(date +%Y.%m.%d_%H.%M.%S)
echo "[START: $which] [$THIS_START] ###############################"


echo $which



if [ "${which}" == "test" ]; then
    contest="tessoku-book"
    contest="abc/abc$2"
    rank=$3

    dir="${HERE}/problems/${contest}/${rank}"
    atcoder-tools "test"  --dir "${dir}"
fi

if [ "${which}" == "submit" ]; then
    contest="abc$2"

    dir="${HERE}/problems/${contest}/${rank}"
    atcoder-tools submit -u --dir "${dir}"
    
fi

if [ "${which}" == sed ]; then
    # find main.py | xargs sed -i "s/\#\!\/home\/k.mikami\/.pyenv\/versions\/atcoder\/bin\/python3.10/\#\!\/usr\/bin\/env python/g"
    # find main.py | xargs sed -i "s/\#\!\/usr\/bin\/env python@/\#\!\/usr\/bin\/env python/g"
    exit
fi


if [ "${which}" == get_files ]; then
    START=
    END=334
    for ((i=START;i<=END;i++)); do
        pb="abc${i}"
        atcoder-tools gen ${pb}
    done
fi

if [ "${which}" == make_pyfiles ]; then
    START=334
    END=334
    ranks=('A' "B" "C" "D" "E" "F" 'G')
    for ((i=START;i<=END;i++)); do
        for rank in "${ranks[@]}"; do
            pb="abc${i}"
            src="${HERE}/utils/template.py"
            dst="${HERE}/problems/${pb}/${rank}/main.py"
            chmod 777 "${dst}"
        done
    done
fi

if [ "${which}" == change_name ]; then
    src="${HERE}"
    python utils/xutils.py --which "${which}" \
        --src "${src}" 2>&1 |  tee "$LOG_DIR/$which.log.$DATE"
fi


if [ "${which}" == git ]; then
    comment=""
    git add . 
    git commit -m "$(date +%Y.%m.%d) $comment"
    git push
fi


THIS_END=$(date +%Y.%m.%d_%H.%M.%S)
echo "[END  : $which] [$THIS_END] ##############################"
