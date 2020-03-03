

        #if request.POST.get('org_type') == 'School':
        max_team_id = Team2020.objects.filter(team_id__contains='2020IRSCPOLICYS').aggregate(Max('team_id'))
        max_team_id = '2020IRSCPOLICYS' + str(max_team_id)
        print(max_team_id)
        max_team_id = int(max_team_id[-3:]) + 1
        tObj = Team2020.objects.create(
            team_id=max_team_id,
            tname=request.POST.get('team_name'),
            institute=request.POST.get('institute'),
            pUser=ppUser,
            teacher=teacherObj,
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            # is_school = request.POST.get('school'), shall we use these fields to identify
            # is_college = request.POST.get('college'),
        )
        leader_name = request.POST.get('team_cordinator_name').split(' ')
        leader_fname = leader_name[0]
        if len(leader_name) > 1:
            leader_lname = leader_name[1]

        leaderObj = Interns2020.objects.create(
            fname=leader_fname,
            lname=leader_lname,
            email=request.POST.get('team_cordinator_email'),
            team=tObj,
            moblie_no=request.POST.get('intern_mobile'),
            org_type=request.POST.get('org_type'),
            is_leader=True,
            city=request.POST.get('city'),
            state=request.POST.get('state'),
        )
        member_2_name = request.POST.get('member_2_name').split(' ')
        mem_2_fname = member_2_name[0]
        if len(member_2_name) > 1:
            mem_2_lname = member_2_name[1]

        Interns2020.objects.create(
            fname=mem_2_fname,
            lname=mem_2_lname,
            email=request.POST.get('member_2_email'),
            team=tObj,
            is_leader=False,

        )

        member_3_name = request.POST.get('member_3_name').split(' ')
        mem_3_fname = member_3_name[0]
        if len(member_3_name) > 1:
            mem_3_lname = member_3_name[1]

        Interns2020.objects.create(

            fname=mem_3_fname,
            lname=mem_3_lname,
            email=request.POST.get('member_3_email'),
            team=tObj,
            is_leader=False,

        )

        member_4_name = request.POST.get('member_4_name').split(' ')
        mem_4_fname = member_4_name[0]
        if len(member_4_name) > 1:
            mem_4_lname = member_4_name[1]
        Interns2020.objects.create(
            fname=mem_4_fname,
            lname=mem_4_lname,
            email=request.POST.get('member_4_email'),
            team=tObj,
            is_leader=False,

        )
        # m_5_fname, m_5_lname = name_checker(request.POST.get('member_5_name'))

        #   m_5_fname,m_5_lname = request.POST.get('member_5_name').split(' ',1)

        member_5_name = request.POST.get('member_5_name').split(' ')
        mem_5_fname = member_5_name[0]
        if len(member_5_name) > 1:
            mem_5_lname = member_5_name[1]

        Interns2020.objects.create(
            fname=mem_5_fname,
            lname=mem_5_lname,
            email=request.POST.get('member_5_email'),
            team=tObj,
            is_leader=False,
        )

        questions = Questions.objects.create(quest1=request.POST.get('question_1'),
                                             quest2=request.POST.get('question_2'),
                                             quest3=request.POST.get('question_3'),
                                             quest4=request.POST.get('question_4'),
                                             quest5=request.POST.get('question_5'),
                                             )
        return render(request, 'policyportal2020/response.html')

""""

        elif request.POST.get('org_type') == 'College':
            max_team_id = Team2020.objects.exclude(team_id__contains='2020IRSCPOLICYS').aggregate(Max('team_id'))
            max_team_id = '2020IRSCPOLICY' + str(max_team_id)
            max_team_id = int(max_team_id[-3:]) + 1
            tObj = Team2020.objects.create(
                team_id=max_team_id,
                tname=request.POST.get('team_name'),
                institute=request.POST.get('institute'),
                pUser=ppUser,
                teacher=teacherObj,
                city=request.POST.get('city'),
                state=request.POST.get('state'),
                # is_school = request.POST.get('school'), shall we use these fields to identify
                # is_college = request.POST.get('college'),
            )

            leaderObj = Interns2020.objects.create(
                fname=leader_fname,
                lname=leader_lname,
                email=request.POST.get('team_cordinator_email'),
                team=tObj,
                moblie_no=request.POST.get('intern_mobile'),
                org_type=request.POST.get('org_type'),
                is_leader=True,
                city=request.POST.get('city'),
                state=request.POST.get('state'),
            )
            member_2_name = request.POST.get('member_2_name').split(' ')
            mem_2_fname = member_2_name[0]
            if len(member_2_name) > 1:
                mem_2_lname = member_2_name[1]

            Interns2020.objects.create(
                fname=mem_2_fname,
                lname=mem_2_lname,
                email=request.POST.get('member_2_email'),
                team=tObj,
                is_leader=False,

            )

            member_3_name = request.POST.get('member_3_name').split(' ')
            mem_3_fname = member_3_name[0]
            if len(member_3_name) > 1:
                mem_3_lname = member_3_name[1]

            Interns2020.objects.create(

                fname=mem_3_fname,
                lname=mem_3_lname,
                email=request.POST.get('member_3_email'),
                team=tObj,
                is_leader=False,

            )

            member_4_name = request.POST.get('member_4_name').split(' ')
            mem_4_fname = member_4_name[0]
            if len(member_4_name) > 1:
                mem_4_lname = member_4_name[1]
            Interns2020.objects.create(
                fname=mem_4_fname,
                lname=mem_4_lname,
                email=request.POST.get('member_4_email'),
                team=tObj,
                is_leader=False,

            )
            # m_5_fname, m_5_lname = name_checker(request.POST.get('member_5_name'))

            #   m_5_fname,m_5_lname = request.POST.get('member_5_name').split(' ',1)

            member_5_name = request.POST.get('member_5_name').split(' ')
            mem_5_fname = member_5_name[0]
            if len(member_5_name) > 1:
                mem_5_lname = member_5_name[1]

            Interns2020.objects.create(
                fname=mem_5_fname,
                lname=mem_5_lname,
                email=request.POST.get('member_5_email'),
                team=tObj,
                is_leader=False,
            )

            questions = Questions.objects.create(quest1=request.POST.get('question_1'),
                                                 quest2=request.POST.get('question_2'),
                                                 quest3=request.POST.get('question_3'),
                                                 quest4=request.POST.get('question_4'),
                                                 quest5=request.POST.get('question_5'),
                                                 )
            return render(request, 'policyportal2020/response.html')


"""