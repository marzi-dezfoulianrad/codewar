def accum(st):
    st=st.lower()
    st=st.split()
    st=[i.capitalize() for i in st]
    st=[i*(st.index(i)+1) for i in st]
    st='-'.join(st)
    return st

#it is not complete need to work on it