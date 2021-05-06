for N in 01 02 03 04 05 06 07 08 09 10
do
  echo "
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nfs-sts-pv${N}
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  nfs:
    server: st01node01
    path: "/mnt/pvs/st01pvol${N}"
" > stspv0${N}.yaml
done
