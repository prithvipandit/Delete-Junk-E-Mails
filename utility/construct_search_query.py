def build_search_query(junk_senders, subjects):
    sender_query = " OR ".join([f"from:{s}" for s in junk_senders])
    subject_query = " OR ".join(subjects)

    full_query = f"({sender_query}) OR ({subject_query}) OR has:unsubscribe"
    return full_query