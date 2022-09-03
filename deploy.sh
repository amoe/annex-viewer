#! /bin/sh

set -eu

remote_host=visarend.solasistim.net
remote_path=/usr/local/lib/annex-viewer


rsync -aPv --exclude-from=exclude.rsf ./ "${remote_host}:${remote_path}"
ssh "$remote_host" touch "${remote_path}/annex-viewer.wsgi"
