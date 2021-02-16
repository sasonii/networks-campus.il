def handle_client_message(conn, cmd, data):
    """
    Gets message code and data and calls the right function to handle command
    Recieves: socket, message code and data
    Returns: None
    """

    global logged_users
    
    if not cmd in chatlib.PROTOCOL_CLIENT.values():
        send_error(conn, "No such command")
    else:
        if not conn.getpeername() in logged_users.keys():
            if cmd == "LOGIN":
                handle_login_message(conn, data)
        else:
            if cmd == "LOGOUT":
                handle_logout_message(conn)
            elif cmd == "MY_SCORE":
                handle_getscore_message(conn, logged_users[conn.getpeername()])
            elif cmd == "HIGHSCORE":
                handle_highscore_message(conn)
            elif cmd == "LOGGED":
                handle_logged_message(conn)
            elif cmd == "GET_QUESTION":
                handle_question_message(conn)
            elif cmd == "SEND_ANSWER":
                handle_answer_message(conn, logged_users[conn.getpeername()], data)
